from typing import cast

from argparse import ArgumentParser

from xmpp_org.build_rfc_list import build_rfc_list
from xmpp_org.build_software_list import build_software_list
from xmpp_org.build_xep_list import build_xep_list
from xmpp_org.lint_software_list import lint_software_list
from xmpp_org.newsletter_email import convert_newsletter_to_email
from xmpp_org.optimize_svg_banners import optimize_svg_banners
from xmpp_org.update_software_entry import update_software_entry

BUILD_RFC_LIST = "build_rfc_list"
BUILD_SOFTWARE_LIST = "build_software_list"
BUILD_XEP_LIST = "build_xep_list"
LINT_SOFTWARE_LIST = "lint_software_list"
UPDATE_SOFTWARE_ENTRY = "update_software_entry"
CONVERT_NEWSLETTER_TO_EMAIL = "convert_newsletter_to_email"
OPTIMIZE_SVG_BANNERS = "optimize_svg_banners"


def create_argparser() -> ArgumentParser:
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(required=True, dest="command")

    subparsers.add_parser(BUILD_RFC_LIST, help="")
    subparsers.add_parser(BUILD_SOFTWARE_LIST, help="")
    subparsers.add_parser(BUILD_XEP_LIST, help="")
    subparsers.add_parser(LINT_SOFTWARE_LIST, help="")

    subparser = subparsers.add_parser(
        UPDATE_SOFTWARE_ENTRY, help="Modify a software entry in the software list."
    )
    subparser.add_argument(
        "name",
        nargs="?",
        default=None,
        metavar="NAME",
        help="Current name of the project",
    )

    subparser.add_argument(
        "--rename",
        dest="new_name",
        metavar="NAME",
        default=None,
        help="Rename the project",
    )

    subparser.add_argument(
        "--set-url",
        dest="new_url",
        metavar="URL",
        default=None,
        help="Change the URL of the project",
    )

    parser.add_argument(
        "--set-doap",
        dest="new_doap",
        metavar="URL",
        default=None,
        help="Change the URL of the project DOAP file",
    )

    subparser.add_argument(
        "--set-platforms",
        dest="new_platforms",
        metavar="PLATFORM",
        default=None,
        nargs="+",
        help="Change the contents of the last column",
    )

    subparser.add_argument(
        "--no-ask",
        dest="ask",
        default=True,
        action="store_false",
        help="Do not ask for confirmation before applying changes. ",
    )

    subparsers.add_parser(CONVERT_NEWSLETTER_TO_EMAIL, help="")

    subparser = subparsers.add_parser(
        OPTIMIZE_SVG_BANNERS, help="Minimize size of an svg file."
    )
    subparser.add_argument(
        "filename",
        type=str,
        nargs="+",
        help="Path to svg file, it must end in _source.svg.",
    )
    return parser


def run() -> None:  # noqa: PLR0911
    args = create_argparser().parse_args()

    if args.command == BUILD_RFC_LIST:
        build_rfc_list()
        return

    if args.command == BUILD_SOFTWARE_LIST:
        build_software_list()
        return

    if args.command == BUILD_XEP_LIST:
        build_xep_list()
        return

    if args.command == LINT_SOFTWARE_LIST:
        lint_software_list()
        return

    if args.command == UPDATE_SOFTWARE_ENTRY:
        update_software_entry(
            args.name,
            args.new_name,
            args.new_url,
            args.new_doap,
            args.new_platforms,
            args.ask,
        )
        return

    if args.command == CONVERT_NEWSLETTER_TO_EMAIL:
        convert_newsletter_to_email()
        return

    if args.command == OPTIMIZE_SVG_BANNERS:
        optimize_svg_banners(cast("str", args.filename[0]))
        return
