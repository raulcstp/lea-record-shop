from locust import HttpUser, between, task


class ApiUser(HttpUser):
    wait_time = between(1,1)
    url = "https://pqg5jyv6rl.execute-api.us-east-1.amazonaws.com/dev"

    @task(1)
    def post_order(self):
        headers = {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE2NjA2NDI2NTh9.d2qSGuSnjeuU9eC4W2m6x14tQ2YQbiN9KL1e-OkBry4"
        }
        self.client.post(
            self.url + "/v1/orders",
            headers=headers,
            json={"disk_id": 1, "amount": 1},
        )

    
