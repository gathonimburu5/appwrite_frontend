import requests
from application.config import Config

class EmployeeService():
    def __init__(self):
        self.base_address = Config.BASE_ADDRESS_URL

    def getAllEmployee(self):
        url = f"{self.base_address}/employees"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("documents", [])

    def createEmployee(self, form_data):
        url = f"{self.base_address}/employees"
        response = requests.post(url=url, json=form_data)
        response.raise_for_status()
        return response.json()

    def getEmployeeById(self, emp_id: str):
        url = f"{self.base_address}/employees/{emp_id}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("documents", [])

    def editEmployee(self, empId:str, formData:dict):
        url = f"{self.base_address}/employees/{empId}"
        response = requests.put(url, data=formData)
        response.raise_for_status()
        return response.json()