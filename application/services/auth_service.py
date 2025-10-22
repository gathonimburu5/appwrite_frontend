import requests
from application.config import Config

class AuthService():
    def __init__(self):
        self.base_address = Config.BASE_ADDRESS_URL

    def LoginUser(self, form_data):
        url = f"{self.base_address}/login"
        response = requests.post(url=url, data=form_data)
        response.raise_for_status()
        return response.json()

    def change_password(self, form_data: dict):
        url = f"{self.base_address}/users/change-passord"
        response = requests.put(url, data=form_data)
        response.raise_for_status()
        return response.json()