from locust import HttpUser, task, between

class OlympicsUser(HttpUser):
    wait_time=between(1,2)

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def reccomendations_page(self):
        self.client.get("/recommendations")
    
    @task
    def survey_page(self):
        self.client.get("/survey")
    @task
    def main_dashboard(self):
        self.client.get("/main_dashboard/")
    
    @task
    def main_dashboard(self):
        self.client.get("/survey_dashboard/")
    
    """
    
    @task
    def do_survey(self):
        self.client.post("/survey", json={
            "age": "18-24", 
            "country": "Ireland",
            "gender": "male", 
            "watch_olympics": "every_olympics",
            "how_long": "99", 
            "summer_vs_winter": "summer",
            "sport": "Boxing", 
            "athlete": "Micheal Jordan",
            "follow_olympics": "tv", 
            "become_Olympian": "true",
            }
            )"
            """