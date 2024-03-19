import os
import pytest

from quickcli.cli_app import app
from unittest import mock


@mock.patch.dict(os.environ, {"GITHUB_TOKEN": ""})
@mock.patch.dict(os.environ, {"FRESHDESK_TOKEN": ""})
def test_app__requires_env_vars(caplog):
    with pytest.raises(SystemExit):
        app()

    messages = caplog.messages
    assert "Error: GITHUB_TOKEN environment variable is not set." in messages
    assert "Error: FRESHDESK_TOKEN environment variable is not set." in messages


@mock.patch.dict(os.environ, {"GITHUB_TOKEN": "token-value"})
@mock.patch.dict(os.environ, {"FRESHDESK_TOKEN": "token-value"})
def test_app__respects_env_vars(caplog):
    with pytest.raises(SystemExit):
        app()

    messages = caplog.messages
    assert "Error: GITHUB_TOKEN environment variable is not set." not in messages
    assert "Error: FRESHDESK_TOKEN environment variable is not set." not in messages
