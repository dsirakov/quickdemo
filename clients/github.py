from typing import Optional
from pydantic import BaseModel
import requests
from urllib.parse import urljoin


class GithubUser(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    name: str
    company: str
    blog: str
    location: str
    email: str
    hireable: bool
    bio: str
    twitter_username: Optional[str] = None
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: str
    updated_at: str
    private_gists: int
    total_private_repos: int
    owned_private_repos: int
    disk_usage: int
    collaborators: int
    two_factor_authentication: bool
    plan: Optional[dict] = None


class GithubClient:
    def __init__(self, token) -> None:
        self.base_url = "https://api.github.com"
        self.api_version = "2022-11-28"
        self.token = token
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": f"{self.api_version}",
        }

    def get_authenticated_user(self) -> GithubUser:
        endpoint = "/user"
        response = requests.get(urljoin(self.base_url, endpoint), headers=self.headers)
        response.raise_for_status()

        return GithubUser.model_validate_json(response.json())
