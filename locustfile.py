from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_icu_info(self):
        # Replace 'Sample_MMSA' with a representative MMSA value
        self.client.get("/icu_info/Manhattan,%20KS")

    @task
    def load_hospitals_info(self):
        self.client.get("/hospitals_info")
