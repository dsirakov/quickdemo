import sys
import logging

from quickcli.utils import verify_environment, parse_args
from quickcli.clients.github import GithubClient
from quickcli.clients.freshdesk import FreshdeskClient
from quickcli.mappers import github_to_freshdesk_user_mapper


logger = logging.getLogger(__name__)


def app():

    github_token, freshdesk_token = verify_environment()

    username, subdomain = parse_args(sys.argv[1:])

    githhub_client = GithubClient(github_token)

    freshdesk_client = FreshdeskClient(freshdesk_token, subdomain)

    github_user = githhub_client.get_user(username)

    freshdesk_contact = github_to_freshdesk_user_mapper(github_user)

    created = freshdesk_client.create_contact(freshdesk_contact)

    logger.info("Freshdesk contact created: %s", created.model_dump_json(indent=2))


if __name__ == "__main__":
    app()
