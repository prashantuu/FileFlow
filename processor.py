import os
from pathlib import Path
from dotenv import load_dotenv
from exceptionz import FileNotExistError
from exceptionz import FileTooLargeError
from uploader import upload_file_URL
from whatsapp import send_message
import time
from log_config import logger
import shutil
from datetime import datetime

#info from .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

#importing extensions as list

image_str = os.getenv("IMAGE_EXTENSIONS")
video_str = os.getenv("VIDEO_EXTENSIONS")
message = os.getenv("MESSAGE")
archive_folder = os.getenv("ARCHIVE_FOLDER")

IMAGE_EXTENSIONS = [ext.strip().lower() for ext in image_str.split(',')] if image_str else []
VIDEO_EXTENSIONS = [ext.strip().lower() for ext in video_str.split(',')] if video_str else []

#size limit stuffs
MAX_IMG_SIZE = 10*1024*1024
MAX_VID_SIZE = 100*1024*1024
MAX_RAW_SIZE = 10*1024*1024


SIZE_LIMITS = {
    "image": MAX_IMG_SIZE,
    "video": MAX_VID_SIZE,
    "raw": MAX_RAW_SIZE
}


# check if file exists and is properly copied
def CHECK_FILE(file_path):
    file_path1 = Path(file_path)
    if not os.path.exists(file_path1):
        logger.error(f"{file_path} not found")
        raise FileNotExistError(file_path1)
    else:
        last_size = 0
        req_stable = 3
        stable = 0
        wait_time = 3
        total_wait = 0
        
        while True:
            current_size = os.path.getsize(file_path1)
            if current_size==last_size:
                stable+=1
                if stable >= req_stable:
                    return file_path1
                
            else:
                stable = 0
                last_size=current_size
            
            time.sleep(wait_time)
            total_wait += wait_time
            if total_wait >=60:
                logger.error(f"File Didn't Finish Up Moving in 60 Sec :{file_path1}")
                raise TimeoutError(f"File Didn't Finish Up Moving in 60 Sec :{file_path1}")





#identify the resource type
def resource_type_identify(file_ext):
    ext = file_ext.lower().lstrip('.')
    if ext in IMAGE_EXTENSIONS:
        return "image"
    elif ext in VIDEO_EXTENSIONS:
        return "video"
    else:
        return "raw"
    
#info about file
class filetoupload:
    def __init__(self,path):
        full_path = Path(path)
        self.name = full_path.name
        self.path = str(full_path)
        self.size = os.path.getsize(full_path)
        self.ext = full_path.suffix.lower().lstrip('.')
        self.resource_type = resource_type_identify(self.ext)

#validate File
def validate_file(file_obj):
    limit = SIZE_LIMITS.get(file_obj.resource_type)

    if file_obj.size > limit:
        logger.error(f"{file_obj.path} exceed size limit of {limit}")
        raise FileTooLargeError(file_obj,limit)


#create archive folder if not
if not os.path.exists(archive_folder):
    os.makedirs(archive_folder)

#time of archiving
timestamp = datetime.now().strftime("%Y;%m;%d_%H:%M:%S")

#function to archive with timestamp
def archive(file_path):
    shutil.move(file_path,os.path.join(archive_folder,f"{timestamp} {os.path.basename(file_path)}"))

#Doing the actual stuff
def prossing(file_path):
    CHECK_FILE(file_path)
    file_obj = filetoupload(file_path)
    validate_file(file_obj)
    file_url = upload_file_URL(file_obj)
    send_message(file_url,message)
    archive(file_path)
    










    






