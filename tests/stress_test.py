from locust import HttpUser, between, task


class ApiUser(HttpUser):
    wait_time = 1
    url = "https://pqg5jyv6rl.execute-api.us-east-1.amazonaws.com/dev"

    @task(1)
    def post_order(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFpYmljaSIsImV4cCI6MTY2MDE5MjEzNn0.tUGGMacBKJvcLd96eGu7FjZELqmiSrjZtc3FiyyMcEU"
        headers = {
            "token": token
        }
        self.client.post(
            self.url + "/v1/orders",
            headers=headers,
            json={"disk_id": 1, "amount": 1},
        )

    
