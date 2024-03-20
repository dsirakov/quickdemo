from quickcli.clients.github import GithubUser
from quickcli.clients.freshdesk import FreshdeskContact


def github_to_freshdesk_user_mapper(github_user: GithubUser) -> FreshdeskContact:
    freshdesk_contact = FreshdeskContact(
        name=github_user.name,
        email=github_user.email,
        twitter_id=github_user.twitter_username,
        unique_external_id=str(github_user.id),
        description=f"Contact imported from Github: {github_user.bio}",
    )

    return freshdesk_contact
