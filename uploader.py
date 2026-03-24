import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv
from pathlib import Path
from log_config import logger

#info from .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

#importing APIS
Api_key = os.getenv("CLOUDINARY_API_KEY")
Api_secret = os.getenv("CLOUDINARY_API_SECRET")
Cloud_name = os.getenv("CLOUD_NAME")

if not Api_key or not Api_secret or not Cloud_name:
    logger.error("Clound API info not found in .env")
    raise ValueError("CRITICAL ERROR: API keys/Cloud Name not found. Check your .env file.")
    

#Configuration
cloudinary.config(
    cloud_name = Cloud_name,
    api_key = Api_key,
    api_secret = Api_secret
)

#upload the file
def upload_file_URL(file_obj):
    result = cloudinary.uploader.upload(file_obj.path,resource_type=file_obj.resource_type,type="upload")
    file_url =  result["secure_url"]
    logger.info(f"{file_obj.path} uploaded with url :{file_url} ")
    return file_url

