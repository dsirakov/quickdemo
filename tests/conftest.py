import pytest


FRESHDESK_TOKEN = "token-value"


@pytest.fixture
def freshdesk_contact():
    return {
        "name": "some name",
        "email": "some email",
        "twitter_id": "some twitter_id",
        "unique_external_id": "some unique external id",
        "description": "some description",
    }


@pytest.fixture
def created_contact():
    return {
        "active": "false",
        "address": "null",
        "company_id": 23,
        "view_all_tickets": "false",
        "deleted": "false",
        "description": "null",
        "email": "superman@freshdesk.com",
        "id": 432,
        "job_title": "null",
        "language": "en",
        "mobile": "null",
        "name": "Super Man",
        "phone": "null",
        "time_zone": "Chennai",
        "twitter_id": "null",
        "other_emails": ["lex@freshdesk.com", "louis@freshdesk.com"],
        "other_companies": [
            {"company_id": 25, "view_all_tickets": "true"},
            {"company_id": 26, "view_all_tickets": "false"},
        ],
        "created_at": "2015-08-28T09:08:16Z",
        "updated_at": "2015-08-28T09:08:16Z",
        "tags": [],
        "avatar": "null",
    }


@pytest.fixture
def github_user():
    return {
        "login": "octocat",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octocat",
        "html_url": "https://github.com/octocat",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "type": "User",
        "site_admin": "false",
        "name": "monalisa octocat",
        "company": "GitHub",
        "blog": "https://github.com/blog",
        "location": "San Francisco",
        "email": "octocat@github.com",
        "hireable": "false",
        "bio": "There once was...",
        "twitter_username": "monatheoctocat",
        "public_repos": 2,
        "public_gists": 1,
        "followers": 20,
        "following": 0,
        "created_at": "2008-01-14T04:33:35Z",
        "updated_at": "2008-01-14T04:33:35Z",
        "private_gists": 81,
        "total_private_repos": 100,
        "owned_private_repos": 100,
        "disk_usage": 10000,
        "collaborators": 8,
        "two_factor_authentication": "true",
        "plan": {
            "name": "Medium",
            "space": 400,
            "private_repos": 20,
            "collaborators": 0,
        },
    }
