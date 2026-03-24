from watchdog.observers import Observer
from watcher import Handler
import time
from dotenv import load_dotenv
from pathlib import Path
import os
from concurrent.futures import ThreadPoolExecutor



# create Pool Executor
executor = ThreadPoolExecutor(max_workers=5)

#info from .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

watch_folder = os.getenv("WATCH_FOLDER")

#main funciton
def main():
    
    event_handler = Handler(executor)
    observer = Observer()
    observer.schedule(event_handler,watch_folder,recursive=False)
    
    observer.start()

    try:
        while observer.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        executor.shutdown


    observer.join()

if __name__=="__main__":
    main()