from pydantic import BaseModel
import requests
from urllib.parse import urljoin


class GithubUser(BaseModel):
    login: str


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
