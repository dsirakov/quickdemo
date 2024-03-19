from quickcli.clients.github import GithubUser
from quickcli.clients.freshdesk import FreshdeskContact


def github_to_freshdesk_user_mapper(github_user: GithubUser) -> FreshdeskContact:
    freshdesk_contact = FreshdeskContact(
        name=github_user.name,
        email=github_user.email,
        # no phone properties in Github but mandatory in Freshdesk
        phone="555-555-555",
        mobile="555-555-555",
        twitter_id=github_user.twitter_username,
        unique_external_id=str(github_user.id),
        description=f"Contact imported from Github: {github_user.bio}",
    )

    return freshdesk_contact
