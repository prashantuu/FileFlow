from dotenv import load_dotenv
from pathlib import Path
import os
from twilio.rest import Client
from exceptionz import MessageNotSentError
from log_config import logger


#info from .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


#importing APIS
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
sender = os.getenv("SENDER_NUMBER")
receiver = os.getenv("RECEIVER_NUMBER")


if not account_sid or not auth_token or not sender or not receiver:
    logger.error("whatsapp stuffs required not found in .env file")
    raise ValueError("CRITICAL ERROR: whatsapp stuffs required not found. Check your .env file.")

#create client
client = Client(account_sid, auth_token)

#send the message
def send_message(file_url,message_to_send):
        try:
            message = client.messages.create(body=message_to_send,
                        media_url=[file_url],
                        from_=sender,
                        to=receiver)
            if  (message.status=="failed"):
                logger.error(f"File of url :{file_url} not Sent")
                raise MessageNotSentError(file_url)
            
            logger.info(f"Sent file of url {file_url} Successfully Message SID: {message.sid}")
        
        except Exception as e:
             logger.error(f"File of url :{file_url} not Sent  : {str(e)}")
             raise MessageNotSentError(file_url)



