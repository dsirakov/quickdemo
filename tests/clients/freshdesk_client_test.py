from urllib.parse import urljoin
import pytest
import json
import responses
from requests import HTTPError
from requests.auth import HTTPBasicAuth
from quickcli.clients.freshdesk import FreshdeskClient, FreshdeskContact, CreatedContact
from unittest.mock import patch, call


FRESHDESK_TOKEN = "token-value"
SUBDOMAIN = "domain"


@pytest.fixture(scope="module")
def mock_client() -> FreshdeskClient:
    return FreshdeskClient(FRESHDESK_TOKEN, SUBDOMAIN)


def test_create_contact__ok(mock_client, freshdesk_contact, created_contact):
    expected_url = urljoin(f"https://{SUBDOMAIN}.freshdesk.com", "/api/v2/contacts")
    expected_headers = {"Content-Type": "application/json"}
    contact_to_create = FreshdeskContact.model_validate(freshdesk_contact)

    with patch("requests.post") as mock_request:
        mock_request.return_value.json.return_value = json.dumps(created_contact)
        created = mock_client.create_contact(contact_to_create)

        assert mock_request.call_args == call(
            expected_url,
            headers=expected_headers,
            data=FreshdeskContact.model_dump(contact_to_create),
            auth=HTTPBasicAuth(FRESHDESK_TOKEN, "X"),
            timeout=(5, 5),
        )
        assert created == CreatedContact.model_validate(created_contact)


@responses.activate
def test_create_contact__raises_error(mock_client, freshdesk_contact):
    expected_url = urljoin("https://domain.freshdesk.com", "/api/v2/contacts")
    create_contact = FreshdeskContact.model_validate(freshdesk_contact)
    responses.add(responses.POST, expected_url, json={}, status=400)

    with pytest.raises(HTTPError):
        _ = mock_client.create_contact(create_contact)
