from typing import TypedDict

from locust import HttpUser, task


class User(TypedDict):
    id: str
    username: str


class ApiSyncUser(HttpUser):
    API_PREFIX = "users/sync"

    @task
    def get_users(self):
        response = self.client.get(self.API_PREFIX)
        users: list[User] = response.json()
        for user in users:
            user_id = user['id']
            self.client.get(f"{self.API_PREFIX}/{user_id}")
