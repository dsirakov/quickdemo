from mappers import (
    github_to_freshdesk_user_mapper,
    GithubUser,
    FreshdeskContact,
)


def test_github_to_freshdesk_user_mapper(github_user):
    gh_user = GithubUser.model_validate(github_user)
    fd_contact = github_to_freshdesk_user_mapper(gh_user)

    assert isinstance(fd_contact, FreshdeskContact)
    assert fd_contact.name == gh_user.name
    assert fd_contact.email == gh_user.email
    assert fd_contact.phone == "555-555-555"
    assert fd_contact.mobile == "555-555-555"
    assert fd_contact.twitter_id == gh_user.twitter_username

    assert fd_contact.unique_external_id == str(gh_user.id)
    assert fd_contact.description == f"Contact imported from Github: {gh_user.bio}"
