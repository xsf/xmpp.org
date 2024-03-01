"""
Adds compliance ratings to software_list_doap.json via
compliancer (https://code.zash.se/compliancer/)
"""

import json
import os
import subprocess
import sys
from pathlib import Path

from colorama import Fore
from colorama import Style
from packaging.version import Version as V  # noqa: N817
from util import download_file

DOWNLOAD_PATH = Path("downloads")
DATA_PATH = Path("data")
COMPLIANCE_SUITE_URL = "https://xmpp.org/extensions/xep-0479.xml"
COMPLIANCER_BUILD_URL = "https://prosody.im/files/compliance"


def generate_compliance_json() -> None:
    """
    Runs the 'compliancer' tool to generate a 'comppliance_suite.json' file
    """
    try:
        result = subprocess.check_output(
            [
                "lua",
                f"{DOWNLOAD_PATH}/compliancer",
                "-v",
                f"{DOWNLOAD_PATH}/compliance-suite.xml",
            ]
        )
        json_result = json.loads(result)
        with open(
            DATA_PATH / "compliance_suite.json", "w", encoding="utf-8"
        ) as compliance_suite_file:
            json.dump(json_result, compliance_suite_file, indent=4)
    except subprocess.CalledProcessError as err:
        print(err)


def check_packages_compliance() -> None:
    """
    Runs the 'compliancer' tool against every package's DOAP file and adds the
    result to '{clients,libraries,servers}_list.doap'
    """

    def add_compliance_data() -> None:
        with open(DATA_PATH / "software_list_doap.json", "rb") as json_file:
            package_list = json.load(json_file)

        for name, props in package_list.items():
            compliance_data = compliance_dict.pop(name, None)
            if compliance_data is None:
                props["badges"] = {}
                continue

            props["badges"] = compliance_data["badges"]

        with open(
            DATA_PATH / "software_list_doap.json", "w", encoding="utf-8"
        ) as clients_data_file:
            json.dump(package_list, clients_data_file, indent=4)

    compliance_dict: dict[str, dict[str, str | dict[str, list[str]]]] = {}

    for subdir, _dirs, files in os.walk(f"{DOWNLOAD_PATH}/doap_files"):
        for file in sorted(files):
            try:
                result = subprocess.check_output(
                    [
                        "lua",
                        f"{DOWNLOAD_PATH}/compliancer",
                        "-v",
                        f"{DOWNLOAD_PATH}/compliance-suite.xml",
                        os.path.join(subdir, file),
                    ]
                )
                json_result = json.loads(result.decode("unicode_escape"))
                compliance_dict[json_result["name"]] = json_result
                badges = json_result["badges"]
                print(
                    f"{Fore.LIGHTBLUE_EX}Compliance checked:{Style.RESET_ALL}",
                    json_result["name"],
                    f"{Fore.MAGENTA}{badges}{Style.RESET_ALL}"
                    if badges
                    else f"{Fore.YELLOW}No level{Style.RESET_ALL}",
                )
            except subprocess.CalledProcessError as err:
                print(f"{Fore.LIGHTRED_EX}{err}{Style.RESET_ALL}")

    add_compliance_data()

    for _name, props in compliance_dict.items():
        if props["badges"]:
            print(
                f"{Fore.YELLOW}Compliance data available, but no match for"
                f"{Style.RESET_ALL}:",
                props["name"],
            )


if __name__ == "__main__":
    # Make sure we're using Lua >= 5.2
    lua_version_string = subprocess.check_output(["lua", "-v"]).decode(
        "unicode_escape"
    )[4:9]
    if V(lua_version_string) < V("5.2.0"):
        print("Lua >= 5.2.0 required")
        sys.exit(1)

    download_file(COMPLIANCE_SUITE_URL, Path("compliance-suite.xml"))
    download_file(COMPLIANCER_BUILD_URL, Path("compliancer"))
    generate_compliance_json()
    check_packages_compliance()
