from urllib.parse import urljoin
import pytest
import json
import responses
from requests import HTTPError
from requests.auth import HTTPBasicAuth
from clients.freshdesk import FreshdeskClient, FreshdeskContact
from unittest.mock import patch, call


FRESHDESK_TOKEN = "token-value"
FRESHDESK_CONTACT = {
    "name": "some name",
    "email": "some email",
    "phone": "some phone",
    "mobile": "some mobile",
    "twitter_id": "some twitter_id",
    "unique_external_id": "some unique external id",
}


@pytest.fixture(scope="module")
def mock_client() -> FreshdeskClient:
    return FreshdeskClient(FRESHDESK_TOKEN)


def test_create_contact__ok(mock_client):
    expected_url = urljoin("https://domain.freshdesk.com", "/api/v2/contacts")
    expected_headers = {"Content-Type": "application/json"}
    create_contact = FreshdeskContact.model_validate(FRESHDESK_CONTACT)

    with patch("requests.post") as mock_request:
        mock_request.return_value.json.return_value = json.dumps({})
        _ = mock_client.create_contact(create_contact)

        assert mock_request.call_args == call(
            expected_url,
            headers=expected_headers,
            data=FreshdeskContact.model_dump(create_contact),
            auth=HTTPBasicAuth(FRESHDESK_TOKEN, "X"),
        )


@responses.activate
def test_create_contact__raises_error(mock_client):
    expected_url = urljoin("https://domain.freshdesk.com", "/api/v2/contacts")
    create_contact = FreshdeskContact.model_validate(FRESHDESK_CONTACT)
    responses.add(responses.POST, expected_url, json={}, status=400)

    with pytest.raises(HTTPError):
        _ = mock_client.create_contact(create_contact)