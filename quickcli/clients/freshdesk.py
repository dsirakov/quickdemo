from pydantic import BaseModel, model_validator
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
from typing import Optional


class FreshdeskContact(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    mobile: Optional[str] = None
    twitter_id: Optional[str] = None
    unique_external_id: str = None
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

    @model_validator(mode="after")
    def check_mandatory_fields(self) -> "FreshdeskContact":
        """
        Validate mandatory fields.
        """
        if not (
            self.phone or self.mobile or self.twitter_id or self.unique_external_id
        ):
            raise ValueError(
                "At least one of 'phone', 'mobile', 'twitter_id or 'unique_external_id' should be set."
            )
        return self


class CreatedContact(BaseModel):
    active: bool
    address: Optional[str] = None
    view_all_tickets: bool
    deleted: bool
    description: Optional[str] = None
    email: str
    id: int
    job_title: Optional[str] = None
    language: Optional[str] = None
    phone: Optional[str] = None
    name: str
    mobile: Optional[str] = None
    time_zone: Optional[str] = None
    twitter_id: Optional[str] = None
    other_emails: Optional[list[str]] = None
    tags: Optional[list[str]] = None
    avatar: Optional[bytes] = None
    created_at: str
    updated_at: str


class FreshdeskClient:
    def __init__(self, token: str, subdomain: str) -> None:
        self.base_url = f"https://{subdomain}.freshdesk.com"
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
        }
        self.auth = HTTPBasicAuth(token, "X")
        self.timeout = (5, 5)

    def create_contact(self, contact: FreshdeskContact) -> CreatedContact:
        endpoint = "/api/v2/contacts"
        data = FreshdeskContact.model_dump(contact)
        response = requests.post(
            urljoin(self.base_url, endpoint),
            headers=self.headers,
            auth=self.auth,
            data=data,
            timeout=self.timeout,
        )
        response.raise_for_status()

        return CreatedContact.model_validate_json(response.json())
