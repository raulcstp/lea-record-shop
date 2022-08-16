import os
from dotenv import load_dotenv
from locust import HttpUser, between, task

load_dotenv()
class ApiUser(HttpUser):
    wait_time = between(1, 1)
    url = (
        "http://localhost:5000"
        if os.environ.get("env") == "DEV"
        else "https://z7gnv4re0c.execute-api.us-east-1.amazonaws.com/dev"
    )
    token = None

    @task(1)
    def post_order(self):
        if not self.token:
            self.client.auth = ("test", "123")
            response = self.client.post(
                url=self.url + "/v1/authenticate",
            )
            self.token = response.json().get("token")
        headers = {
            "token": self.token,
        }
        self.client.post(
            url=self.url + "/v1/orders",
            headers=headers,
            json={"disk_id": 1, "amount": 1},
        )
