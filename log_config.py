import logging 
import os


#funciton to log stuffs
def make_logger():

    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s -  %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/Flow.log"),
            logging.StreamHandler()
        ]
    )

    # Mute Twilio's detailed HTTP logs
    logging.getLogger('twilio.http_client').setLevel(logging.WARNING)

    # Mute the connection pool warnings
    logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)

    # Mute Cloudinary (if it starts chatting too much)
    logging.getLogger('cloudinary').setLevel(logging.WARNING)
    
    return logging.getLogger("FileFlow")

    

logger = make_logger()