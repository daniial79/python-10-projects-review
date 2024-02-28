from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class MainScreen(Screen):
    def get_image_link(self) -> str:
        query = self.manager.current_screen.ids.user_query.text
        return wikipedia.page(query).images[0]
        
    def download_image(self, link: str) -> str:
        response = requests.get(link)
        image_path = "files/output.jpg"
        with open(image_path, "wb") as file:
            file.write(response.content)
        return image_path
    
    def set_image(self):
        image_link = self.get_image_link()
        image_path = self.download_image(image_link)
        self.manager.current_screen.ids.img.source = image_path
        
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    
    def build(self):
        return RootWidget()
    
MainApp().run()