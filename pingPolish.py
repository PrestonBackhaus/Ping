import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class WebsiteCheckerPolish:
    def __init__(self, source_url):
        self.source_url = source_url
        self.urls = []
        self.used_urls = []
    
    def scrape_urls(self):
        html_text = requests.get(self.source_url).text
        soup = BeautifulSoup(html_text, 'lxml')
        divs = soup.find_all('div', class_='table-responsive')
        for d in divs:
            trs = d.find_all('tr')
            for t in trs:
                link = t.find('a')
                if link and link.get('href'):
                    url = link.get('href')
                    self.urls.append(url)
    
    def polish_urls(self):
        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
        english_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
        for i in range(len(self.urls)):
            parsed_url = urlparse(self.urls[i])
            domain_name = parsed_url.netloc
            domain_name = domain_name.replace('www.', '')
            domain = domain_name.split('.')[0]
            after_domain = domain_name.split('.')[1]
            for j in range(len(polish_chars)):
                domain = domain.replace(english_chars[j], polish_chars[j])
            domain = f'https://{domain}.{after_domain}'
            self.urls[i] = domain
    
    def check_urls(self):
        for i in range(len(self.urls)):
            try:
                response = requests.get(self.urls[i])
                if response.status_code == 200:
                    print(f"{self.urls[i]} is already online.\n\n")
                    self.used_urls.append(self.urls[i])
                else:
                    print(f"{self.urls[i]} is offline. \n\n")
                    self.used_urls.append(self.urls[i])
            except requests.exceptions.RequestException as e:
                print(f"{self.urls[i]} is offline or not in use: {e}")
                print("URL INVALID\n\n")
    
    def print_used_urls(self):
        if len(self.used_urls) == 0:
            print(self.used_urls)
            print("NO URLS IN USE!")
        else:
            print(self.used_urls)
            
    def run(self):
        self.scrape_urls()
        self.polish_urls()
        self.check_urls()
        self.print_used_urls()


checker = WebsiteCheckerPolish('https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites')
checker.run()