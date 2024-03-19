import os
import sys


def verify_environemnt() -> tuple:
    github_token = os.getenv("GITHUB_TOKEN")
    freshdesk_token = os.getenv("FRESHDESK_TOKEN")

    errors = []
    if not github_token:
        errors.append("Error: GITHUB_TOKEN environment variable is not set.")

    if not freshdesk_token:
        errors.append("Error: FRESHDESK_TOKEN environment variable is not set.")

    if errors:
        for error in errors:
            print(error)
        sys.exit(1)

    return github_token, freshdesk_token
