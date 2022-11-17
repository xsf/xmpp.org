'''
Download / prepare / process XMPP DOAP files for the software list
Requires: Pillow, python-slugify
'''
from typing import Optional
from typing import Union

from datetime import date
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import json
import os
import re
import shutil
from urllib.parse import urlparse

from colorama import Fore
from colorama import Style
from defusedxml.ElementTree import parse
from defusedxml.ElementTree import ParseError
from PIL import Image
from PIL import UnidentifiedImageError
from PIL.Image import Resampling
from slugify import slugify

from util import download_file
from util import initialize_directory

SOFTWARE_PATH = Path('content/software')
DATA_PATH = Path('data')
DOWNLOAD_PATH = Path('downloads')
STATIC_PATH = Path('static')
STATIC_DOAP_PATH = STATIC_PATH / 'doap'
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

XML_DECLARATION = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'
XMPP_XSL = '<?xml-stylesheet href=\"/doap/xmpp-style.xsl\" type=\"text/xsl\"?>'

MD_FRONTMATTER = '''---\ntitle: "%s"\ndate: %s\nlayout: packages\n---\n
{{< package-details name_slug="%s" package_type="%s" >}}
'''

PLATFORMS: list[str] = [
    'Android',
    'iOS',
    'Browser',
    'Windows',
    'macOS',
    'Linux',
]

ENTRY_LIFETIME = timedelta(days=365)


def check_renewal(name: str, renewed: Optional[str]) -> bool:
    '''
    Check if 'last_renewed' entry is not older than 365 days
    '''
    if renewed is None:
        return False
    try:
        last_renewal = datetime.strptime(renewed, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        print('Failed to parse timestamp for', name)
        return False
    now = datetime.utcnow()
    if now - last_renewal > ENTRY_LIFETIME:
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
    except (FileNotFoundError, ParseError) as err:
        print('Error while trying to parse DOAP file:', doap_file, err)
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

    info['programming_lang'] = []
    for entry in doap.findall(DOAP_PROGRAMMING_LANGUAGE):
        info['programming_lang'].append(entry.text)

    info['logo'] = None
    doap_logo = doap.find(DOAP_LOGO)
    if doap_logo is not None:
        info['logo'] = doap_logo.attrib[RDF_RESOURCE]

    return info


def check_image_file(file_path: Path, extension: str) -> bool:
    '''
    Check if file size is greater than 300 KiB and if so, resize image
    Returns success
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
                  f'(file size: {file_size / (1<<10):,.0f} KB) '
                  f'has been resized')
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


def prepare_package_data(package_type: str) -> None:
    '''
    Download and prepare package data (clients/servers/libraries) for
    rendering with Hugo
    '''
    print(f'Preparing data from {package_type}.json')
    initialize_directory(SOFTWARE_PATH / package_type)

    with open(DATA_PATH / f'{package_type}.json', 'rb') as json_file:
        xsf_package_list = json.load(json_file)

    package_infos: dict[str, dict[
        str, Union[None, str, list[str], dict[str, str]]]] = {}

    number_of_packages = 0
    number_of_expired_packages = 0
    number_of_doap_packages = 0

    for package in xsf_package_list:
        number_of_packages += 1

        if not check_renewal(
                package['name'], package.get('last_renewed')):
            number_of_expired_packages += 1
            print(f'{Fore.RED}Entry expired'
                  f'{Style.RESET_ALL}    ',
                  package['name'])
            continue

        if package['doap'] is None:
            print(f'{Fore.YELLOW}DOAP n/a'
                  f'{Style.RESET_ALL}         ',
                  package['name'])
            package_infos[package['name']] = {
                    'name_slug': None,
                    'homepage': package['url'],
                    'logo': None,
                    'shortdesc': None,
                    'platforms': package['platforms'],
                    'programming_lang': None,
            }
            continue

        # DOAP is available
        number_of_doap_packages += 1
        package_name_slug = slugify(
            package['name'],
            replacements=[['+', 'plus']])

        doap_url = package['doap']
        if doap_url.startswith('/hosted-doap'):
            # DOAP file is hosted at xmpp.org
            print(f'{Fore.LIGHTCYAN_EX}DOAP by xmpp.org'
                  f'{Style.RESET_ALL} ',
                  package['name'])
            shutil.copyfile(
                f'{STATIC_PATH}{doap_url}',
                Path(f'{DOWNLOAD_PATH}/doap_files/{package_name_slug}.doap'))
        else:
            print(f'{Fore.LIGHTBLUE_EX}DOAP by vendor'
                  f'{Style.RESET_ALL}   ',
                  package['name'])
            download_file(
                package['doap'],
                Path(f'doap_files/{package_name_slug}.doap'))

        parsed_package_infos = parse_doap_infos(package_name_slug)
        if parsed_package_infos is None:
            continue

        logo_uri = None
        logo = parsed_package_infos['logo']
        if logo is not None and isinstance(logo, str):
            logo_uri = process_logo(
                package_name_slug, logo)

        package_infos[package['name']] = {
            'name_slug': package_name_slug,
            'homepage': parsed_package_infos['homepage'],
            'logo': logo_uri,
            'shortdesc': parsed_package_infos['shortdesc'],
            'platforms': parsed_package_infos['platforms'],
            'programming_lang': parsed_package_infos['programming_lang'],
        }

        create_package_page(package_type, package_name_slug, package['name'])

    print(f'Number of {package_type}:\n'
          f'total: {number_of_packages} '
          f'(with DOAP: {number_of_doap_packages}), '
          f'expired: {number_of_expired_packages}\n{42 * "="}')
    with open(DATA_PATH / f'{package_type}_list_doap.json',
              'w',
              encoding='utf-8') as package_data_file:
        json.dump(package_infos, package_data_file, indent=4)


def create_package_page(package_type: str, name_slug: str, name: str) -> None:
    '''
    Create an .md page for package, containing a shortcode
    for displaying package details
    '''
    today = date.today()
    date_formatted = today.strftime('%Y-%m-%d')
    with open(SOFTWARE_PATH / package_type / f'{name_slug}.md',
              'w',
              encoding='utf8') as md_file:
        md_file.write(
            MD_FRONTMATTER % (
                f'XMPP {package_type.capitalize()}: {name}',
                date_formatted,
                name_slug,
                package_type))


def prepare_doap_files() -> None:
    '''
    Copy DOAP files to /static/doap/ and replace the
    xml-stylesheet with our stylesheet (or add it, if there is none)
    '''
    for entry in os.scandir(DOWNLOAD_PATH / 'doap_files'):
        shutil.copy(DOWNLOAD_PATH / 'doap_files' / entry.name,
                    STATIC_DOAP_PATH / entry.name)

    for entry in os.scandir(STATIC_PATH / 'hosted-doap'):
        shutil.copy(STATIC_PATH / 'hosted-doap' / entry.name,
                    STATIC_DOAP_PATH / entry.name)

    xml_declaration_pattern = r'<\?xml version.+?\?>'
    stylesheet_pattern = r'<\?xml-stylesheet.+?\?>'
    for entry in os.scandir(STATIC_DOAP_PATH):
        if not entry.name.endswith('.doap'):
            continue

        with open(STATIC_DOAP_PATH / entry.name, 'r+') as doap_file:
            content = doap_file.read()

            result = re.sub(
                stylesheet_pattern,
                XMPP_XSL,
                content,
                0,
                re.MULTILINE)
            if result != content:
                # Replaced custom stylesheet with our stylesheet
                doap_file.truncate(0)
                doap_file.seek(0)
                doap_file.write(result)
                continue

            # No custom stylesheet found
            result = re.sub(
                xml_declaration_pattern,
                f'{XML_DECLARATION}\n{XMPP_XSL}',
                content,
                0,
                re.MULTILINE)
            if result != content:
                # Added our stylesheet
                doap_file.truncate(0)
                doap_file.seek(0)
                doap_file.write(result)
            else:
                print('WARNING: Could not alter XML header of', entry.name)
                # Remove content entirely, since we can't
                # control what would be rendered
                doap_file.truncate(0)


if __name__ == '__main__':
    initialize_directory(DOWNLOAD_PATH)
    initialize_directory(LOGOS_PATH)
    Path(DOWNLOAD_PATH / 'doap_files').mkdir(parents=True)

    prepare_package_data('clients')
    prepare_package_data('libraries')
    prepare_package_data('servers')

    initialize_directory(STATIC_DOAP_PATH)
    prepare_doap_files()
