"""Download / prepare / process XMPP DOAP files for the software list
Requires: Pillow, python-slugify
"""

from typing import Any

import json
import os
import re
import shutil
from datetime import datetime
from datetime import UTC
from pathlib import Path
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

SOFTWARE_PATH = Path("content/software")
DATA_PATH = Path("data")
DOWNLOAD_PATH = Path("downloads")
STATIC_PATH = Path("static")
STATIC_DOAP_PATH = STATIC_PATH / "doap"
THEMES_PATH = Path("themes")
LOGOS_PATH = STATIC_PATH / "images" / "packages"

DOAP_NS = "http://usefulinc.com/ns/doap#"
XMPP_NS = "https://linkmauve.fr/ns/xmpp-doap#"
SCHEMA_NS = "https://schema.org/"
RDF_RESOURCE = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
DOAP_NAME = f".//{{{DOAP_NS}}}name"
DOAP_SHORTDESC = f".//{{{DOAP_NS}}}shortdesc"
DOAP_HOMEPAGE = f".//{{{DOAP_NS}}}homepage"
DOAP_DOWNLOAD_PAGE = f".//{{{DOAP_NS}}}download-page"
DOAP_SUPPORT_FORUM = f".//{{{DOAP_NS}}}support-forum"
DOAP_OS = f".//{{{DOAP_NS}}}os"
DOAP_CODE_REPO = f".//{{{DOAP_NS}}}repository"
DOAP_CODE_REPO_BROWSE = f".//{{{DOAP_NS}}}browse"
DOAP_PROGRAMMING_LANGUAGE = f".//{{{DOAP_NS}}}programming-language"
DOAP_LOGO = f".//{{{SCHEMA_NS}}}logo"
DOAP_IMPLEMENTS = f".//{{{DOAP_NS}}}implements"
DOAP_SUPPORTED_XEP = f".//{{{XMPP_NS}}}SupportedXep"
DOAP_XEP_NUMBER = f".//{{{XMPP_NS}}}xep"
DOAP_XEP_VERSION = f".//{{{XMPP_NS}}}version"
DOAP_XEP_STATUS = f".//{{{XMPP_NS}}}status"
DOAP_XEP_SINCE = f".//{{{XMPP_NS}}}since"

RFC_REGEX = r"rfc\d{1,4}"
XEP_REGEX = r"xep-\d{1,4}"

XML_DECLARATION = '<?xml version="1.0" encoding="UTF-8"?>'
XMPP_XSL = '<?xml-stylesheet href="/doap/xmpp-style.xsl" type="text/xsl"?>'

MD_FRONTMATTER = """---
title: "%(title)s"
date: %(date)s
layout: packages
aliases:
    - "/software/%(type)s/%(name_slug)s"
---

{{< software-details name_slug="%(name_slug)s" package_type="%(type)s" >}}
"""

SOFTWARE_CATEGORIES: list[str] = [
    "client",
    "component",
    "library",
    "server",
    "tool",
]
PLATFORMS: list[str] = [
    "Android",
    "iOS",
    "Browser",
    "Windows",
    "macOS",
    "Linux",
]

DoapInfoT = dict[str, str | list[str] | list[dict[str, str | None]] | None] | None


def parse_doap_infos(doap_file: str) -> DoapInfoT:
    """Parse DOAP file and return infos"""
    try:
        doap = parse(DOWNLOAD_PATH / f"doap_files/{doap_file}.doap")
    except (FileNotFoundError, ParseError) as err:
        print("Error while trying to parse DOAP file:", doap_file, err)
        return None

    info: dict[str, str | list[str] | list[dict[str, str | None]] | None] = {}

    info["name"] = None
    doap_name = doap.find(DOAP_NAME)
    if doap_name is not None:
        info["name"] = doap_name.text

    info["homepage"] = None
    doap_homepage = doap.find(DOAP_HOMEPAGE)
    if doap_homepage is not None:
        info["homepage"] = doap_homepage.attrib.get(RDF_RESOURCE)

    info["shortdesc"] = None
    doap_shortdesc = doap.find(DOAP_SHORTDESC)
    if doap_shortdesc is not None:
        info["shortdesc"] = doap_shortdesc.text

    info["download_page"] = None
    doap_download_page = doap.find(DOAP_DOWNLOAD_PAGE)
    if doap_download_page is not None:
        info["download_page"] = doap_download_page.attrib.get(RDF_RESOURCE)

    info["support_forum"] = None
    doap_support_forum = doap.find(DOAP_SUPPORT_FORUM)
    if doap_support_forum is not None:
        info["support_forum"] = doap_support_forum.attrib.get(RDF_RESOURCE)

    info["platforms"] = []
    for entry in doap.findall(DOAP_OS):
        if entry.text is not None:
            info["platforms"].append(entry.text)

    info["code_repository"] = None
    doap_code_repository = doap.find(DOAP_CODE_REPO)
    if doap_code_repository is not None:
        repos = doap_code_repository.findall(".//*")
        for element in repos:
            browse_element = element.find(DOAP_CODE_REPO_BROWSE)
            if browse_element is not None:
                info["code_repository"] = browse_element.attrib.get(RDF_RESOURCE)
                break

    info["programming_lang"] = []
    for entry in doap.findall(DOAP_PROGRAMMING_LANGUAGE):
        if entry.text is not None:
            info["programming_lang"].append(entry.text)

    info["logo"] = None
    doap_logo = doap.find(DOAP_LOGO)
    if doap_logo is not None:
        info["logo"] = doap_logo.attrib.get(RDF_RESOURCE)

    rfcs: list[str] = []
    xeps: list[dict[str, str | None]] = []
    for entry in doap.findall(DOAP_IMPLEMENTS):
        rfc = entry.attrib.get(RDF_RESOURCE)
        if rfc is not None:
            match = re.search(RFC_REGEX, rfc)
            if match:
                rfcs.append(match.group()[3:])

        supported_xep = entry.find(DOAP_SUPPORTED_XEP)
        if supported_xep is not None:
            number = supported_xep.find(DOAP_XEP_NUMBER)
            if number is not None:
                number = number.attrib.get(RDF_RESOURCE)
                match = re.search(XEP_REGEX, number or "")
                if match:
                    number = match.group()[4:]

            version = supported_xep.find(DOAP_XEP_VERSION)
            if version is not None:
                version = version.text

            status = supported_xep.find(DOAP_XEP_STATUS)
            if status is not None:
                status = status.text

            since = supported_xep.find(DOAP_XEP_SINCE)
            if since is not None:
                since = since.text

            xeps.append(
                {
                    "number": number,
                    "version": version,
                    "status": status,
                    "since": since,
                },
            )

    info["rfcs"] = rfcs
    info["xeps"] = xeps

    return info


def check_image_file(file_path: Path, extension: str) -> bool:
    """Check if file size is greater than 300 KiB and if so, resize image
    Returns success
    """
    if extension == "svg":
        # No need to resize SVG files
        return True

    try:
        file_size = file_path.stat().st_size
    except OSError as error:
        print("An error occurred while trying to open logo:", error)
        return False

    if file_size <= 300000:
        # Small enough, no need to resize image
        return True

    try:
        with Image.open(file_path) as img:
            width, height = img.size
            new_width = 400
            new_height = int(new_width * height / width)
            resized_img = img.resize((new_width, new_height), Resampling.LANCZOS)
            resized_img.save(file_path)
            print(
                f"                  Logo at {file_path} "
                f"(file size: {file_size / (1 << 10):,.0f} KB) "
                f"too big, had to be resized",
            )
    except (ValueError, OSError, UnidentifiedImageError) as error:
        print("An error occurred while trying to resize logo:", error)
        return False

    return True


def process_logo(package_name: str, uri: str) -> str | None:
    """Download package logo and return logo URI"""
    image_url = urlparse(uri)
    extension = Path(image_url.path).suffix
    file_name = f"{package_name}{extension}"
    success = download_file(uri, Path(file_name))
    if not success:
        return None

    success = check_image_file(DOWNLOAD_PATH / file_name, extension[1:].lower())
    if not success:
        return None
    logo_uri = f"/images/packages/{package_name}{extension}"
    shutil.copyfile(DOWNLOAD_PATH / file_name, Path(LOGOS_PATH / file_name))
    return logo_uri


def prepare_package_data() -> None:
    """Download and prepare package data (software.json) for
    rendering with Hugo
    """
    shutil.copy(SOFTWARE_PATH / "_index.md", DOWNLOAD_PATH / "software_index.md")
    shutil.copy(
        SOFTWARE_PATH / "software-comparison.md",
        DOWNLOAD_PATH / "software-comparison.md",
    )
    initialize_directory(SOFTWARE_PATH)
    shutil.copy(DOWNLOAD_PATH / "software_index.md", SOFTWARE_PATH / "_index.md")
    shutil.copy(
        DOWNLOAD_PATH / "software-comparison.md",
        SOFTWARE_PATH / "software-comparison.md",
    )

    with Path(DATA_PATH / "software.json").open("rb") as json_file:
        xsf_package_list = json.load(json_file)

    package_infos: dict[str, Any] = {}

    number_of_doap_packages = 0

    for package in xsf_package_list:
        if package["doap"] is None:
            print(f"{Fore.YELLOW}DOAP n/a{Style.RESET_ALL}         ", package["name"])
            continue

        # DOAP is available
        number_of_doap_packages += 1
        package_name_slug = slugify(package["name"], replacements=[["+", "plus"]])

        doap_url = package["doap"]
        if doap_url.startswith("/hosted-doap"):
            # DOAP file is hosted at xmpp.org
            print(
                f"{Fore.LIGHTCYAN_EX}DOAP by xmpp.org{Style.RESET_ALL} ",
                package["name"],
            )
            shutil.copyfile(
                f"{STATIC_PATH}{doap_url}",
                Path(f"{DOWNLOAD_PATH}/doap_files/{package_name_slug}.doap"),
            )
        else:
            print(
                f"{Fore.LIGHTBLUE_EX}DOAP by vendor{Style.RESET_ALL}   ",
                package["name"],
            )
            download_file(package["doap"], Path(f"doap_files/{package_name_slug}.doap"))

        parsed_package_infos = parse_doap_infos(package_name_slug)
        if parsed_package_infos is None:
            continue

        logo_uri = None
        logo = parsed_package_infos["logo"]
        if logo is not None and isinstance(logo, str):
            logo_uri = process_logo(package_name_slug, logo)

        package_infos[package["name"]] = {
            "categories": package["categories"],
            "name_slug": package_name_slug,
            "homepage": parsed_package_infos["homepage"],
            "logo": logo_uri,
            "shortdesc": parsed_package_infos["shortdesc"],
            "download_page": parsed_package_infos["download_page"],
            "code_repository": parsed_package_infos["code_repository"],
            "support_forum": parsed_package_infos["support_forum"],
            "platforms": parsed_package_infos["platforms"],
            "programming_lang": parsed_package_infos["programming_lang"],
            "rfcs": parsed_package_infos["rfcs"],
            "xeps": parsed_package_infos["xeps"],
        }

        for category in package["categories"]:
            package_category = "libraries" if category == "library" else f"{category}s"
            create_package_page(package_category, package_name_slug, package["name"])

    print(
        f"\n{42 * '='}\n"
        f"Number of packages\n"
        f"Total: {len(xsf_package_list)}\n"
        f"With DOAP: {number_of_doap_packages} "
        f"({round(number_of_doap_packages / len(xsf_package_list) * 100, 1)} %)"
        f"\n{42 * '='}",
    )
    with Path(DATA_PATH / "software_list_doap.json").open(
        "w",
        encoding="utf-8",
    ) as package_data_file:
        json.dump(package_infos, package_data_file, indent=4)


def add_doap_data_to_xeplist() -> None:
    """Adds data from DOAP files (implementations) to xeplist.json"""
    with Path(DATA_PATH / "software_list_doap.json").open(
        encoding="utf-8",
    ) as software_list:
        software_data = json.load(software_list)
    with Path(DATA_PATH / "xeplist.json").open(encoding="utf-8") as xep_list:
        xep_data = json.load(xep_list)

    for xep in xep_data:
        xep["implementations"] = []
        for name, package_data in software_data.items():
            if not package_data["xeps"]:
                continue
            for supported_xep in package_data["xeps"]:
                if supported_xep["number"] == f"{xep['number']:04d}":
                    xep["implementations"].append(
                        {
                            "package_name": name,
                            "package_name_slug": package_data["name_slug"],
                            "package_logo": package_data["logo"],
                            "package_categories": package_data["categories"],
                            "implemented_version": supported_xep["version"],
                            "implementation_status": supported_xep["status"],
                            "implementation_since": supported_xep["since"],
                        },
                    )
                    break

    with Path(DATA_PATH / "xeplist.json").open("w", encoding="utf-8") as xep_list:
        json.dump(xep_data, xep_list, indent=4)

    # Store xeplist as JS array in assets path in
    # order to make it available for scripts
    with Path(THEMES_PATH / "xmpp.org" / "static" / "js" / "xeplist.js").open(
        "w",
        encoding="utf-8",
    ) as js_file:
        js_file.write(f"const xepListData = {json.dumps(xep_data)}")


def create_package_page(package_type: str, name_slug: str, name: str) -> None:
    """Create an .md page for package, containing a shortcode
    for displaying package details
    """
    today = datetime.now(tz=UTC).date()
    date_formatted = today.strftime("%Y-%m-%d")
    with Path(SOFTWARE_PATH / f"{name_slug}.md").open("w", encoding="utf-8") as md_file:
        md_file.write(
            MD_FRONTMATTER
            % {
                "title": f"XMPP {package_type.capitalize()}: {name}",
                "date": date_formatted,
                "type": package_type,
                "name_slug": name_slug,
            },
        )


def prepare_doap_files() -> None:
    """Copy DOAP files to /static/doap/ and replace the
    xml-stylesheet with our stylesheet (or add it, if there is none)
    """
    for entry in os.scandir(DOWNLOAD_PATH / "doap_files"):
        shutil.copy(
            DOWNLOAD_PATH / "doap_files" / entry.name,
            STATIC_DOAP_PATH / entry.name,
        )

    for entry in os.scandir(STATIC_PATH / "hosted-doap"):
        shutil.copy(
            STATIC_PATH / "hosted-doap" / entry.name,
            STATIC_DOAP_PATH / entry.name,
        )

    xml_declaration_pattern = r"<\?xml version.+?\?>"
    stylesheet_pattern = r"<\?xml-stylesheet.+?\?>"
    for entry in os.scandir(STATIC_DOAP_PATH):
        if not entry.name.endswith(".doap"):
            continue

        with Path(STATIC_DOAP_PATH / entry.name).open(
            "r+",
            encoding="utf-8",
        ) as doap_file:
            content = doap_file.read()

            result = re.sub(
                stylesheet_pattern,
                XMPP_XSL,
                content,
                count=0,
                flags=re.MULTILINE,
            )
            if result != content:
                # Replaced custom stylesheet with our stylesheet
                doap_file.truncate(0)
                doap_file.seek(0)
                doap_file.write(result)
                continue

            # No custom stylesheet found
            result = re.sub(
                xml_declaration_pattern,
                f"{XML_DECLARATION}\n{XMPP_XSL}",
                content,
                count=0,
                flags=re.MULTILINE,
            )
            if result != content:
                # Added our stylesheet
                doap_file.truncate(0)
                doap_file.seek(0)
                doap_file.write(result)
            else:
                print("WARNING: Could not alter XML header of", entry.name)
                # Remove content entirely, since we can't
                # control what would be rendered
                doap_file.truncate(0)


if __name__ == "__main__":
    initialize_directory(DOWNLOAD_PATH)
    initialize_directory(LOGOS_PATH)
    Path(DOWNLOAD_PATH / "doap_files").mkdir(parents=True)

    prepare_package_data()
    add_doap_data_to_xeplist()

    initialize_directory(STATIC_DOAP_PATH)
    prepare_doap_files()
