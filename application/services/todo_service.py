import requests
from application.config import Config

class ToDoService():
    def __init__(self):
        self.base_address = Config.BASE_ADDRESS_URL

    def get_todo(self):
        url = f"{self.base_address}/todos"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("documents", [])

    def create_todo(self, form_data):
        url = f"{self.base_address}/todos"
        response = requests.post(url=url, json=form_data)
        response.raise_for_status()
        return response.json()

    def get_todo_id(self, todo_id: str):
        url = f"{self.base_address}/todos/{todo_id}"