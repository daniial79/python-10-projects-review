import requests
from selectorlib import Extractor

class Temprature:
    def __init__(self, city, country):
        self.city = "-".join(city.split())
        self.country = country    
    
    def get(self):
        essential_headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        response = requests.get(f"https://timeanddate/weather/{self.country}/{self.city}", headers=essential_headers)
        content = response.text
        
        extractor = Extractor.from_yaml_file('temperature.yaml')
        data = extractor.extract(content)
        temperature = float(data.split("\\")[0])
        
        return temperature