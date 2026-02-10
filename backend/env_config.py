from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Secret Key
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # Database Info
    NAME = os.getenv('NAME')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    ENGINE = os.getenv('ENGINE')
    
    
