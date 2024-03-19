import argparse

from quickcli.utils import verify_environment
from quickcli.clients.github import GithubClient
from quickcli.clients.freshdesk import FreshdeskClient
from quickcli.mappers import github_to_freshdesk_user_mapper


def app():

    github_token, freshdesk_token = verify_environment()

    parser = argparse.ArgumentParser(description="Quickdemo CLI app")
    parser.add_argument("username", help="Github username")
    parser.add_argument("subdomain", help="Freshdesk subdomain")
    args = parser.parse_args()

    username = args.username
    subdomain = args.subdomain

    githhub_client = GithubClient(github_token)
    freshdesk_client = FreshdeskClient(freshdesk_token, subdomain)

    github_user = githhub_client.get_user(username)
    freshdesk_contact = github_to_freshdesk_user_mapper(github_user)
    freshdesk_client.create_contact(freshdesk_contact)

    # Print a greeting
    print(f"Hello, {username}!")
    print(f"Hello, {subdomain}!")


if __name__ == "__main__":
    app()
