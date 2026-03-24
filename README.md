# FileFlow

An event-driven file processing pipeline that automatically detects files in a folder, validates them, uploads them to cloud storage, and sends them via WhatsApp.

## 🚀Features

📂 Folder monitoring using watchdog
⏳ File stability check (prevents incomplete uploads)
📦 Supports images, videos, and raw files
☁️ Cloud upload integration with Cloudinary
💬 WhatsApp messaging using Twilio
⚙️ Configurable via environment variables
📦 File Archived After Process
🗒️ Loggings of Processes

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

i absolutely have no idea. this is some lame waste of time but i asked chatgpt and behold the reason : 

This project was built to explore event-driven architecture, file system monitoring, and handling real-world issues like file stability, concurrency,external API integration and blah blah waste of time. 

## 🤖 AI Assistance

ofc i used chatgpt and Gemini, this is my first ever project and i don't have any mentor who would told me about Structure of a Projects and stuff 

This project was developed with the assistance of AI as a learning and productivity tool.

AI was primarily used for Mentorship regarding Best Practices for Project Preparation

it helped me with:
- understanding how system designs and architecures are made
- Understanding system design concepts such as e concurrency
- Debugging issues and refining implementation approaches
- Gaining insights into best practices for structuring and scaling the system
 and this readme.md

AND this is not some ai slop
All core implementation, integration, and decision-making were carried out by me 
lil bit of Codes from Chatgpt/Gemini where used for concurrency as i had no idea about it but i do now
Learnt Cloudinary and Twilio stuffs from the Docs available

## 📗 Application

nothing

