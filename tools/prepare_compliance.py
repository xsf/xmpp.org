from typing import Union

import json
import os
import subprocess
from pathlib import Path

from colorama import Fore
from colorama import Style

from util import download_file

DOWNLOAD_PATH = Path('downloads')
DATA_PATH = Path('data')
COMPLIANCE_SUITE_URL = 'https://xmpp.org/extensions/xep-0459.xml'
COMPLIANCER_BUILD_URL = 'https://prosody.im/files/compliance'


def generate_compliance_json() -> None:
    '''
    Runs the 'compliancer' tool to generate a 'comppliance_suite.json' file
    '''
    try:
        result = subprocess.check_output([
            'lua5.4',
            f'{DOWNLOAD_PATH}/compliancer',
            '-v',
            f'{DOWNLOAD_PATH}/compliance-suite.xml'])
        json_result = json.loads(result)
        with open(DATA_PATH / 'compliance_suite.json',
                  'w',
                  encoding='utf-8') as compliance_suite_file:
            json.dump(json_result, compliance_suite_file, indent=4)
    except subprocess.CalledProcessError as err:
        print(err)


def check_packages_compliance() -> None:
    '''
    Runs the 'compliancer' tool against every package's DOAP file and adds the
    result to '{clients,libraries,servers}_list.doap'
    '''
    def add_compliance_data() -> None:
        with open(DATA_PATH / 'software_list_doap.json',
                  'rb') as json_file:
            package_list = json.load(json_file)

        for name, props in package_list.items():
            compliance_data = compliance_dict.pop(name, None)
            if compliance_data is None:
                props['badges'] = {}
                continue

            props['badges'] = compliance_data['badges']

        with open(DATA_PATH / 'software_list_doap.json',
                  'w',
                  encoding='utf-8') as clients_data_file:
            json.dump(package_list, clients_data_file, indent=4)

    compliance_dict: dict[
        str, dict[str, Union[str, dict[str, list[str]]]]] = {}

    for subdir, _dirs, files in os.walk(f'{DOWNLOAD_PATH}/doap_files'):
        for file in files:
            try:
                result = subprocess.check_output([
                    'lua5.4',
                    f'{DOWNLOAD_PATH}/compliancer',
                    '-v',
                    f'{DOWNLOAD_PATH}/compliance-suite.xml',
                    os.path.join(subdir, file)])
                json_result = json.loads(result.decode('unicode_escape'))
                compliance_dict[json_result['name']] = json_result
            except subprocess.CalledProcessError as err:
                print(err)

    add_compliance_data()

    for _name, props in compliance_dict.items():
        if props['badges']:
            print(f'{Fore.YELLOW}Compliance data available, but no match for'
                  f'{Style.RESET_ALL}:',
                  props['name'])


if __name__ == '__main__':
    download_file(
        COMPLIANCE_SUITE_URL, Path('compliance-suite.xml'))
    download_file(COMPLIANCER_BUILD_URL, Path('compliancer'))
    generate_compliance_json()
    check_packages_compliance()
