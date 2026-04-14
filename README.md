# FileFlow

An event-driven file processing pipeline that automatically detects files in a folder, validates them, uploads them to cloud storage, and sends them via WhatsApp.
Made it with the sole objective to learn.

## 🚀Features

- 📂 Folder monitoring using watchdog
- ⏳ File stability check (prevents incomplete uploads)
- 📦 Supports images, videos, and raw files
- ☁️ Cloud upload integration with Cloudinary
- 💬 WhatsApp messaging using Twilio
- ⚙️ Configurable via environment variables
- 📦 File Archived After Process
- 🗒️ Loggings of Processes

## 🧠 How It Works

Pipeline architecture:

Watcher → Processor → Uploader → Messenger -> Archiver

- Watcher : detects new files in a specified folder
- Processor : ensures file is stable and valid
- Uploader : sends file to cloud and gets URL(Cloudinary API)
- Messenger : sends the file via WhatsApp(Twilio API)
- Archiver : Archives the files Processed

## 🛠️ Tech Stack

Python
watchdog
Cloudinary
Twilio

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/prashantuu/FileFlow.git
cd FileFlow
```
2. Create virtual environment
```bash
python -m venv env
```
#Linux :
 ```bash 
source env/bin/activate
```  
#Windows :
```bash
 env\Scripts\activate
 ```
3. Install dependencies using pip package manager
```bash
pip install -r requirements.txt
```
4. Create .env file

Add the following:
```
CLOUD_NAME=cloudinary_cloud_name
CLOUDINARY_API_KEY=cloudinary_api_keys
CLOUDINARY_API_SECRET=cloudinary_api_secret_keys

ACCOUNT_SID=twilio_account_sid
AUTH_TOKEN=twilio_auth_token
SENDER_NUMBER=whatsapp:+twilio_number
RECEIVER_NUMBER=whatsapp:+number_of_reciever

IMAGE_EXTENSIONS=jpg,jpeg,png,gif,webp(Cloudinary Supported)
VIDEO_EXTENSIONS=mp4,mov,avi,mkv(Cloudinary Supported)

WATCH_FOLDER=foldepath_to_watch
ARCHIVE_FOLDER=folderpath_to_archive

MESSAGE=message_to_send
```

5. Run the project
```bash
python main.py
```

## 💡 Why This Project
 to explore event-driven architecture, file system monitoring, and handling real-world issues like file stability, concurrency and external API integration

