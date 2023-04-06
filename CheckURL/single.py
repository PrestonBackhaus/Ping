import requests
from urllib.parse import urlparse

class SingleChecker:
    def __init__(self, source_url):
        self.output = ''
        self.source_url = source_url
        self.urls = []
        self.trueURLs = []
        
    def polish(self):
        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
        english_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
        top = ['.com', '.org', '.net', '.gov', '.edu', '.mil', '.int', '.info', '.biz', '.name', '.pro', '.coop', '.mobi', '.travel', '.jobs', '.tel']
        http = self.source_url.split(':')[0]
        domain = urlparse(self.source_url).netloc
        domain = domain.replace('www.','')
        after_domain = domain.split('.')[1]
        domain = domain.split('.')[0]
        for i in range(len(polish_chars)):
            domain = domain.replace(english_chars[i], polish_chars[i])
        self.urls = [f'{http}://www.{domain}{t}' for t in top]
        
    def checkURL(self, url):
        if url=='':
            print('URL INVALID\n\n')
            self.output = 'URL INVALID\n\n'
        else:
            try:
                response = requests.get(url) 
                if response.status_code == 200:
                    print(f'{url} is already online.\n\n')
                    self.output = f'{url} is already online.\n\n'
                    self.trueURLs.append(url)
                else:
                    print(f'{url} is offline.\n\n')
                    self.output = f'{url} is offline.\n\n'
            except requests.exceptions.RequestException as e:
                print(f'{url} is offline or not in use: {e}')
                print('URL INVALID\n\n')
                self.output = f'{url} is offline or not in use: {e}\nURL INVALID'
            
    def getOutput(self):
        return self.output

            
    def run(self):
        self.polish()
        self.checkURL(self.source_url)
        for url in self.urls:
            self.checkURL(url)
        return self.trueURLs
    