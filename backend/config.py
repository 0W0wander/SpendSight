import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev')
    DEBUG = True
    UPLOAD_FOLDER = BASE_DIR / 'data/uploads'
    ALLOWED_EXTENSIONS = {'csv'}
    
    @staticmethod
    def init_app():
        Config.UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
