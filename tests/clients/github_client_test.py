from urllib.parse import urljoin
import pytest
import json
import responses
from requests import HTTPError
from quickcli.clients.github import GithubClient, GithubUser
from unittest.mock import patch, call


GITHUB_TOKEN = "token-value"
GITHUB_USERNAME = "octocat"


@pytest.fixture(scope="module")
def mock_client() -> GithubClient:
    return GithubClient(GITHUB_TOKEN)


def test_get_user__ok(mock_client, github_user):
    username = "octocat"
    expected_url = urljoin("https://api.github.com", f"/user/{username}")
    expected_headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    with patch("requests.get") as mock_request:
        mock_request.return_value.json.return_value = json.dumps(github_user)
        user = mock_client.get_user(GITHUB_USERNAME)

        assert mock_request.call_args == call(expected_url, headers=expected_headers)
        assert user == GithubUser.model_validate(github_user)


@responses.activate
def test_get_user__raises_error(mock_client):
    username = "octocat"
    expected_url = urljoin("https://api.github.com", f"/user/{username}")

    responses.add(responses.GET, expected_url, json={}, status=400)

    with pytest.raises(HTTPError):
        _ = mock_client.get_user(GITHUB_USERNAME)
