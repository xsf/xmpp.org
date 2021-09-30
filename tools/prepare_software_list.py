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
LOGOS_PATH = STATIC_PATH / 'images' / 'clients'

DOAP_NS = 'http://usefulinc.com/ns/doap#'
SCHEMA_NS = 'https://schema.org/'
RDF_RESOURCE = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource'
DOAP_NAME = f'.//{{{DOAP_NS}}}name'
DOAP_SHORTDESC = f'.//{{{DOAP_NS}}}shortdesc'
DOAP_OS = f'.//{{{DOAP_NS}}}os'
DOAP_LOGO = f'.//{{{SCHEMA_NS}}}logo'

PLATFORMS: list[str] = [
    'Android',
    'iOS',
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
        print('Client entry expired for', name)
        return False
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

    info['shortdesc'] = None
    doap_shortdesc = doap.find(DOAP_SHORTDESC)
    if doap_shortdesc is not None:
        info['shortdesc'] = doap_shortdesc.text

    info['os'] = []
    for entry in doap.findall(DOAP_OS):
        info['os'].append(entry.text)
    if not info['os']:
        info['os'] = ['Other']

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


def process_logo(client_name: str, uri: str) -> Optional[str]:
    '''
    Download client logo and return logo URI
    '''
    image_url = urlparse(uri)
    _, extension = os.path.splitext(image_url.path)
    file_name = f'{client_name}{extension}'
    success = download_file(
        uri,
        Path(file_name))
    if not success:
        return None

    success = check_image_file(
        DOWNLOAD_PATH / file_name, extension[1:].lower())
    if not success:
        return None
    logo_uri = f'/images/clients/{client_name}{extension}'
    shutil.copyfile(
        DOWNLOAD_PATH / file_name,
        Path(LOGOS_PATH / file_name))
    return logo_uri


def prepare_clients_list() -> None:
    '''
    Download and prepare clients data
    '''
    with open(DATA_PATH / 'clients.json', 'rb') as json_file:
        xsf_clients_list = json.load(json_file)

    client_infos: dict[str, list[dict[str, Optional[str]]]] = {}
    for platform in PLATFORMS:
        client_infos[platform] = []
    client_infos['Other'] = []

    number_of_clients = 0
    number_of_expired_clients = 0
    number_of_doap_clients = 0

    for client in xsf_clients_list:
        number_of_clients += 1

        if not check_renewal(
                client['name'], client.get('last_renewed')):
            number_of_expired_clients += 1
            continue

        if client['doap'] is None:
            added_to_other = False
            for client_os in cast(list[str], client['platforms']):
                added_to_os = False
                for platform in PLATFORMS:
                    if platform.lower() not in client_os.lower():
                        continue
                    added_to_os = True
                    client_infos[platform].append(
                        {
                            'name': client['name'],
                            'url': client['url'],
                            'logo': None,
                            'shortdesc': None,
                            'os': client_os
                        }
                    )
                if not added_to_os and not added_to_other:
                    added_to_other = True
                    client_infos['Other'].append(
                        {
                            'name': client['name'],
                            'url': client['url'],
                            'logo': None,
                            'shortdesc': None,
                            'os': client['platforms']
                        }
                    )
            continue

        number_of_doap_clients += 1
        client_name = slugify(client['name'])

        download_file(
            client['doap'],
            Path(f'doap_files/{client_name}.doap'))
        parsed_client_infos = parse_doap_infos(client_name)
        if parsed_client_infos is None:
            continue

        logo_uri = None
        if parsed_client_infos['logo'] is not None:
            logo_uri = process_logo(client_name, parsed_client_infos['logo'])

        added_to_other = False
        for client_os in parsed_client_infos['os']:
            added_to_os = False
            for platform in PLATFORMS:
                if platform.lower() not in client_os.lower():
                    continue
                added_to_os = True
                client_infos[platform].append(
                    {
                        'name': client['name'],
                        'url': client['url'],
                        'logo': logo_uri,
                        'shortdesc': parsed_client_infos['shortdesc'],
                        'os': client_os
                    }
                )
            if not added_to_os and not added_to_other:
                added_to_other = True
                client_infos['Other'].append(
                    {
                        'name': client['name'],
                        'url': client['url'],
                        'logo': logo_uri,
                        'shortdesc': parsed_client_infos['shortdesc'],
                        'os': parsed_client_infos['os']
                    }
                )

    print(f'Number of clients (total: {number_of_clients}, '
          f'expired: {number_of_expired_clients}, '
          f'with DOAP: {number_of_doap_clients})')
    with open(DATA_PATH / 'clients_list_doap.json',
              'w',
              encoding='utf-8') as client_data_file:
        json.dump(client_infos, client_data_file, indent=4)


if __name__ == '__main__':
    initialize_directory(DOWNLOAD_PATH)
    initialize_directory(LOGOS_PATH)
    Path(DOWNLOAD_PATH / 'doap_files').mkdir(parents=True)
    prepare_clients_list()
