import pytest
from quickcli.cli_app import app


def test_app__requires_env_vars(caplog):
    with pytest.raises(SystemExit):
        app()

    messages = caplog.messages
    assert "Error: GITHUB_TOKEN environment variable is not set." in messages
    assert "Error: FRESHDESK_TOKEN environment variable is not set." in messages
