
from filestack import Client

class FileSharer:
    def __init__(self, api_token: str, filepath: str):
        self.api_token = api_token
        self.filepath = filepath
    
    def share(self) -> str:
        client = Client(self.api_token)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url

class Webcam:
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def capture(self):
        pass