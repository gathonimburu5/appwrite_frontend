import requests
from application.config import Config

class SupplierService():
    def __init__(self):
        self.base_address = Config.BASE_ADDRESS_URL

    def getAllSupplier(self):
        url = f"{self.base_address}/suppliers"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def createSupplier(self, formData:dict):
        url = f"{self.base_address}/suppliers"
        res = requests.post(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def getSupplierById(self, supplierId:str):
        url = f"{self.base_address}/suppliers/{supplierId}"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def updateSupplier(self, supplierId:str, formData:dict):
        url = f"{self.base_address}/suppliers/{supplierId}"
        res = requests.put(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def activateSupplier(self, supplierId:str, formData:dict):
        url = f"{self.base_address}/suppliers_activate/{supplierId}"
        res = requests.put(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def deactivateSupplier(self, supplierId:str, fData:dict):
        url = f"{self.base_address}/suppliers_deactivate/{supplierId}"
        res = requests.put(url=url, data=fData)
        res.raise_for_status()
        return res.json()

    def getActiveSupplier(self):
        url = f"{self.base_address}/active_suppliers"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])