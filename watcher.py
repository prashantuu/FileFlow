
from watchdog.events import FileSystemEventHandler
from processor import prossing
from log_config import logger



class Handler(FileSystemEventHandler):
    def __init__(self,executor_plugin):
        super().__init__()
        self.executor = executor_plugin
    def on_created(self,event):
        logger.info(f"Queued : {event.src_path}")
        self.executor.submit(prossing,event.src_path)
        


