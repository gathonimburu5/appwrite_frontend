import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    BASE_ADDRESS_URL= os.getenv('BASE_ADDRESS')

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass