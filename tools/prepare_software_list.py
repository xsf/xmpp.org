'''
Download / prepare / process XMPP DOAP files for the software list
Requires: Pillow, python-slugify
'''
from typing import Optional
from typing import Union
from typing import cast

from datetime import datetime
from datetime import timedelta
from pathlib import Path
import json
import os
import shutil
from urllib.parse import urlparse

from defusedxml.ElementTree import parse
from defusedxml.ElementTree import ParseError
import requests
from PIL import Image
from PIL import UnidentifiedImageError
from PIL.Image import Resampling
from slugify import slugify

DOWNLOAD_PATH = Path('downloads')
DATA_PATH = Path('data')
STATIC_PATH = Path('static')
LOGOS_PATH = STATIC_PATH / 'images' / 'packages'

DOAP_NS = 'http://usefulinc.com/ns/doap#'
SCHEMA_NS = 'https://schema.org/'
RDF_RESOURCE = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource'
DOAP_NAME = f'.//{{{DOAP_NS}}}name'
DOAP_SHORTDESC = f'.//{{{DOAP_NS}}}shortdesc'
DOAP_HOMEPAGE = f'.//{{{DOAP_NS}}}homepage'
DOAP_OS = f'.//{{{DOAP_NS}}}os'
DOAP_PROGRAMMING_LANGUAGE = f'.//{{{DOAP_NS}}}programming-language'
DOAP_LOGO = f'.//{{{SCHEMA_NS}}}logo'

PLATFORMS: list[str] = [
    'Android',
    'iOS',
    'Browser',
    'Windows',
    'macOS',
    'Linux',
]

ENTRY_LIFETIME = timedelta(days=365)


def initialize_directory(path: Path) -> None:
    '''
    Remove path (if it exists) and containing files, then recreate path
    '''
    if path.exists() and path.is_dir():
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)


def download_file(url: str, path: Path) -> bool:
    '''
    Downloads file from url and stores it in /downloads/path
    returns success
    '''
    file_request = requests.get(url, stream=True, timeout=5)
    if not 200 >= file_request.status_code < 400:
        print('Error while trying to download from', url)
        return False

    with open(DOWNLOAD_PATH / path, 'wb') as data_file:
        max_size = 1024 * 1024 * 10  # 10 MiB
        size = 0
        for chunk in file_request.iter_content(chunk_size=8192):
            data_file.write(chunk)
            size += len(chunk)
            if size > max_size:
                file_request.close()
                print('File size exceeds 10 MiB:', path)
                return False
    return True


def check_renewal(name: str, renewed: Optional[str]) -> bool:
    '''
    Check if 'last_renewed' entry is not older than 365 days
    '''
    if renewed is None:
        return False
    try:
        renewed = datetime.strptime(renewed, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        print('Failed to parse timestamp for', name)
        return False
    now = datetime.utcnow()
    if now - renewed > ENTRY_LIFETIME:
        print('Package entry expired for', name)
        return False
    print('Package entry up to date for', name)
    return True


def parse_doap_infos(doap_file: str
                     ) -> Optional[dict[str, Union[str, list[str], None]]]:
    '''
    Parse DOAP file and return infos
    '''
    try:
        doap = parse(
            DOWNLOAD_PATH / f'doap_files/{doap_file}.doap')
    except (FileNotFoundError, ParseError):
        return None

    info: dict[str, Union[str, list[str], None]] = {}

    info['name'] = None
    doap_name = doap.find(DOAP_NAME)
    if doap_name is not None:
        info['name'] = doap_name.text

    info['homepage'] = None
    doap_homepage = doap.find(DOAP_HOMEPAGE)
    if doap_homepage is not None:
        info['homepage'] = doap_homepage.attrib[RDF_RESOURCE]

    info['shortdesc'] = None
    doap_shortdesc = doap.find(DOAP_SHORTDESC)
    if doap_shortdesc is not None:
        info['shortdesc'] = doap_shortdesc.text

    info['platforms'] = []
    for entry in doap.findall(DOAP_OS):
        info['platforms'].append(entry.text)
    if not info['platforms']:
        info['platforms'] = ['Other']

    info['programming_lang'] = []
    for entry in doap.findall(DOAP_PROGRAMMING_LANGUAGE):
        info['programming_lang'].append(entry.text)
    if not info['programming_lang']:
        info['programming_lang'] = ['Other']

    info['logo'] = None
    doap_logo = doap.find(DOAP_LOGO)
    if doap_logo is not None:
        info['logo'] = doap_logo.attrib[RDF_RESOURCE]

    return info


def check_image_file(file_path: Path, extension: str) -> None:
    '''
    Check if file size is greater than 300 KiB and if so, resize image
    '''
    if extension == 'svg':
        # No need to resize SVG files
        return True

    try:
        file_size = os.path.getsize(file_path)
    except OSError as error:
        print('An error occurred while trying to open logo:', error)
        return False

    if file_size <= 300000:
        # Small enough, no need to resize image
        return True

    try:
        with Image.open(file_path) as img:
            width, height = img.size
            new_width = 400
            new_height = int(new_width * height / width)
            img = img.resize(
                (new_width, new_height), Resampling.LANCZOS)
            img.save(file_path)
            print(f'Logo at {file_path} '
                  f'(file size: {file_size}) has been resized')
    except (ValueError, OSError, UnidentifiedImageError) as error:
        print('An error occurred while trying to resize logo:', error)
        return False

    return True


def process_logo(package_name: str, uri: str) -> Optional[str]:
    '''
    Download package logo and return logo URI
    '''
    image_url = urlparse(uri)
    _, extension = os.path.splitext(image_url.path)
    file_name = f'{package_name}{extension}'
    success = download_file(
        uri,
        Path(file_name))
    if not success:
        return None

    success = check_image_file(
        DOWNLOAD_PATH / file_name, extension[1:].lower())
    if not success:
        return None
    logo_uri = f'/images/packages/{package_name}{extension}'
    shutil.copyfile(
        DOWNLOAD_PATH / file_name,
        Path(LOGOS_PATH / file_name))
    return logo_uri


def prepare_package_list(package_type: str) -> None:
    '''
    Download and prepare data (clients/servers/libraries)
    '''
    with open(DATA_PATH / f'{package_type}.json', 'rb') as json_file:
        xsf_package_list = json.load(json_file)

    package_infos: dict[str, list[dict[str, Optional[str]]]] = {}
    if package_type == 'libraries':
        platforms = []
    else:
        platforms = PLATFORMS

    for platform in platforms:
        package_infos[platform] = []
    package_infos['Other'] = []

    number_of_packages = 0
    number_of_expired_packages = 0
    number_of_doap_packages = 0

    for package in xsf_package_list:
        number_of_packages += 1

        if not check_renewal(
                package['name'], package.get('last_renewed')):
            number_of_expired_packages += 1
            continue

        if package['doap'] is None:
            added_to_other = False
            for package_platform in cast(list[str], package['platforms']):
                added_to_platform = False
                for platform in platforms:
                    if platform.lower() not in package_platform.lower():
                        continue
                    added_to_platform = True
                    package_infos[platform].append(
                        {
                            'name': package['name'],
                            'homepage': package['url'],
                            'logo': None,
                            'shortdesc': None,
                            'platforms': package_platform
                        }
                    )
                if not added_to_platform and not added_to_other:
                    added_to_other = True
                    package_infos['Other'].append(
                        {
                            'name': package['name'],
                            'homepage': package['url'],
                            'logo': None,
                            'shortdesc': None,
                            'platforms': package['platforms']
                        }
                    )
            continue

        # DOAP is available
        number_of_doap_packages += 1
        package_name = slugify(package['name'])

        doap_url = package['doap']
        if doap_url.startswith('/doap'):
            # DOAP file is hosted at xmpp.org
            shutil.copyfile(
                f'{STATIC_PATH}{doap_url}',
                Path(f'{DOWNLOAD_PATH}/doap_files/{package_name}.doap'))
        else:
            download_file(
                package['doap'],
                Path(f'doap_files/{package_name}.doap'))

        parsed_package_infos = parse_doap_infos(package_name)
        if parsed_package_infos is None:
            continue

        logo_uri = None
        if parsed_package_infos['logo'] is not None:
            logo_uri = process_logo(package_name, parsed_package_infos['logo'])

        added_to_other = False
        for package_platform in parsed_package_infos['platforms']:
            added_to_platform = False
            for platform in platforms:
                if platform.lower() not in package_platform.lower():
                    continue
                added_to_platform = True
                package_infos[platform].append(
                    {
                        'name': package['name'],
                        'homepage': parsed_package_infos['homepage'],
                        'logo': logo_uri,
                        'shortdesc': parsed_package_infos['shortdesc'],
                        'platforms': package_platform,
                        'programming_lang': parsed_package_infos[
                            'programming_lang'],
                    }
                )
            if not added_to_platform and not added_to_other:
                added_to_other = True
                package_infos['Other'].append(
                    {
                        'name': package['name'],
                        'homepage': parsed_package_infos['homepage'],
                        'logo': logo_uri,
                        'shortdesc': parsed_package_infos['shortdesc'],
                        'platforms': parsed_package_infos['platforms'],
                        'programming_lang': parsed_package_infos[
                            'programming_lang'],
                    }
                )

    print(f'Number of packages (total: {number_of_packages}, '
          f'expired: {number_of_expired_packages}, '
          f'with DOAP: {number_of_doap_packages})')
    with open(DATA_PATH / f'{package_type}_list_doap.json',
              'w',
              encoding='utf-8') as package_data_file:
        json.dump(package_infos, package_data_file, indent=4)


if __name__ == '__main__':
    initialize_directory(DOWNLOAD_PATH)
    initialize_directory(LOGOS_PATH)
    Path(DOWNLOAD_PATH / 'doap_files').mkdir(parents=True)
    prepare_package_list('clients')
    prepare_package_list('libraries')
    prepare_package_list('servers')
