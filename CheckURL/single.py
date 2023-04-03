import requests
from urllib.parse import urlparse

class SingleChecker:
    def __init__(self, source_url):
        self.output = ''
        self.source_url = source_url
        self.found_urls = []
        
    def polish(self):
        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
        english_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
        http = self.source_url.split(':')[0]
        domain = urlparse(self.source_url).netloc
        domain = domain.replace('www.','')
        after_domain = domain.split('.')[1]
        domain = domain.split('.')[0]
        for i in range(len(polish_chars)):
            domain = domain.replace(english_chars[i], polish_chars[i])
        self.source_url = f'{http}://www.{domain}.{after_domain}'
        
    def checkURL(self):
        try:
            response = requests.get(self.source_url)
            if response.status_code == 200:
                print(f'{self.source_url} is already online.\n\n')
                self.output = f'{self.source_url} is already online.\n\n'
            else:
                print(f'{self.source_url} is offline.\n\n')
                self.output = f'{self.source_url} is offline.\n\n'
        except requests.exceptions.RequestException as e:
            print(f'{self.source_url} is offline or not in use: {e}')
            print('URL INVALID\n\n')
            self.output = f'{self.source_url} is offline or not in use: {e}\nURL INVALID'
            
    def getOutput(self):
        return self.output
            
    def run(self):
        self.polish()
        self.checkURL()
        return self.output
        