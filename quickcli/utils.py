import os
import sys
import logging
import argparse

logger = logging.getLogger(__name__)


def verify_environment() -> tuple:
    github_token = os.getenv("GITHUB_TOKEN")
    freshdesk_token = os.getenv("FRESHDESK_TOKEN")

    errors = []
    if not github_token:
        errors.append("Error: GITHUB_TOKEN environment variable is not set.")

    if not freshdesk_token:
        errors.append("Error: FRESHDESK_TOKEN environment variable is not set.")

    if errors:
        for error in errors:
            logger.error(error)
        sys.exit(1)

    return github_token, freshdesk_token


def parse_args(args: list):
    parser = argparse.ArgumentParser(description="Quickdemo CLI app")
    parser.add_argument("username", help="Github username")
    parser.add_argument("subdomain", help="Freshdesk subdomain")
    parsed = parser.parse_args(args)

    return parsed.username, parsed.subdomain
