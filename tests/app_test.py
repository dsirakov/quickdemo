import os
import sys
import pytest

from unittest.mock import patch, call

from quickcli.cli_app import app
from quickcli.clients.github import GithubClient, GithubUser
from quickcli.clients.freshdesk import FreshdeskClient, FreshdeskContact


@patch.dict(os.environ, {"GITHUB_TOKEN": ""})
@patch.dict(os.environ, {"FRESHDESK_TOKEN": ""})
def test_app__requires_env_vars(caplog):
    with pytest.raises(SystemExit):
        app()

    messages = caplog.messages
    assert "Error: GITHUB_TOKEN environment variable is not set." in messages
    assert "Error: FRESHDESK_TOKEN environment variable is not set." in messages


@patch.dict(os.environ, {"GITHUB_TOKEN": "gh-token-value"})
@patch.dict(os.environ, {"FRESHDESK_TOKEN": "fd-token-value"})
@pytest.mark.parametrize(
    "sys_argv, exepcted_log",
    [
        (
            ["quickcli"],
            "usage: quickcli [-h] username subdomain\nquickcli: error: the following arguments are required: username, subdomain\n",
        ),
        (
            ["quickcli", "cool_programmer"],
            "usage: quickcli [-h] username subdomain\nquickcli: error: the following arguments are required: subdomain\n",
        ),
    ],
    ids=["no arguments", "one argument only"],
)
def test_app__requires_arguments(capfd, sys_argv, exepcted_log):
    with pytest.raises(SystemExit):
        with patch.object(sys, "argv", sys_argv):
            app()

    _, err = capfd.readouterr()
    assert err
    assert err == exepcted_log


@patch.dict(os.environ, {"GITHUB_TOKEN": "gh-token-value"})
@patch.dict(os.environ, {"FRESHDESK_TOKEN": "fd-token-value"})
@patch.object(sys, "argv", ["quickcli", "cool_programmer", "mydomain"])
def test_app__logic(github_user, freshdesk_contact):
    github_user_model = GithubUser.model_validate(github_user)
    freshdesk_contact_model = FreshdeskContact.model_validate(freshdesk_contact)

    with patch(
        "quickcli.clients.github.GithubClient.__init__", return_value=None
    ) as gh_client_init, patch(
        "quickcli.clients.freshdesk.FreshdeskClient.__init__", return_value=None
    ) as fd_client_init, patch.object(
        GithubClient, "get_user", return_value=github_user_model
    ) as get_user_mock, patch.object(
        FreshdeskClient, "create_contact"
    ) as create_contact_mock, patch(
        "quickcli.cli_app.github_to_freshdesk_user_mapper",
        return_value=freshdesk_contact_model,
    ) as mapper_mock:
        app()

    assert gh_client_init.call_args == call("gh-token-value")
    assert fd_client_init.call_args == call("fd-token-value", "mydomain")
    assert get_user_mock.call_args == call("cool_programmer")
    assert mapper_mock.call_args == call(github_user_model)
    assert create_contact_mock.call_args == call(freshdesk_contact_model)
