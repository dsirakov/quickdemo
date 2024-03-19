from pydantic import BaseModel
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
from typing import Optional


class FreshdeskContact(BaseModel):
    name: str
    email: str
    phone: str
    mobile: str
    twitter_id: str
    unique_external_id: str
    other_emails: Optional[list[str]] = None
    company_id: Optional[int] = None
    view_all_tickets: Optional[bool] = None
    other_companies: Optional[list[str]] = None
    address: Optional[str] = None
    avatar: Optional[bytes] = None
    custom_fields: Optional[dict] = None
    description: Optional[str] = None
    job_title: Optional[str] = None
    language: Optional[str] = None
    tags: Optional[list[str]] = None
    time_zone: Optional[str] = None
    lookup_parameter: Optional[str] = None


class FreshdeskClient:
    def __init__(self, token) -> None:
        self.base_url = "https://domain.freshdesk.com"
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
        }
        self.auth = HTTPBasicAuth(token, "X")

    def create_contact(self, contact: FreshdeskContact) -> str:
        endpoint = "/api/v2/contacts"
        data = FreshdeskContact.model_dump(contact)
        response = requests.post(
            urljoin(self.base_url, endpoint),
            headers=self.headers,
            auth=self.auth,
            data=data,
        )
        response.raise_for_status()

        return response.json()
