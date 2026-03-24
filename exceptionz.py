class FileValidationError(Exception):
    pass

class WhatsappMessageError(Exception):
    pass


class FileNotExistError(FileValidationError):
    def __init__(self,file_path):
        self.path = file_path
        message = f"File doesn't exist in path : {file_path}"
        super().__init__(message)


class FileTooLargeError(FileValidationError):
    def __init__(self, file_obj, limit):
        self.file = file_obj
        self.limit = limit
        message = f"{file_obj.name} ({file_obj.size} bytes) exceeds limit of {limit} bytes"
        super().__init__(message)


class MessageNotSentError(WhatsappMessageError):
    def __init__(self, url):
        self.url = url
        message = f"{url} was not sent"
        super().__init__(message)


