import os
import secrets
from dotenv import load_dotenv

load_dotenv()

class Config():
    BASE_ADDRESS_URL= os.getenv('BASE_ADDRESS')
    SECRET_KEY = secrets.token_hex(16)

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass