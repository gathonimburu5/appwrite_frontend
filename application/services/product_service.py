import requests
from application.config import Config

class ProductService():
    def __init__(self):
        self.base_address = Config.BASE_ADDRESS_URL

    def getAllProducts(self):
        url = f"{self.base_address}/products"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def createProduct(self, formData:dict):
        url = f"{self.base_address}/products"
        res = requests.post(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def getProductPerId(self, productId:str):
        url = f"{self.base_address}/products/{productId}"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def editProduct(self, productId:str, formData:dict):
        url = f"{self.base_address}/products/{productId}"
        res = requests.put(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def getAllCategory(self):
        url = f"{self.base_address}/categories"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def createCategory(self, formData:dict):
        url = f"{self.base_address}/categories"
        res = requests.post(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def getCategoryById(self, catId:str):
        url = f"{self.base_address}/categories/{catId}"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def updateCategory(self, catId:str, formData:dict):
        url = f"{self.base_address}/categories/{catId}"
        res = requests.put(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def getAllMeasureUnit(self):
        url = f"{self.base_address}/measure-units"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def createMeasureUnit(self, formData:dict):
        url = f"{self.base_address}/measure-units"
        res = requests.post(url=url, data=formData)
        res.raise_for_status()
        return res.json()

    def getMeasureUnitPerId(self, unitId:str):
        url = f"{self.base_address}/measure-units/{unitId}"
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        return data.get("documents", [])

    def updateMeasureUnit(self, unitId:str, formData:dict):
        url = f"{self.base_address}/measure-units/{unitId}"
        res = requests.put(url=unitId, data=formData)
        res.raise_for_status()
        return res.json()
