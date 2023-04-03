import requests
from bs4 import BeautifulSoup

class WebsiteCheckerPolishMini:
    
    def __init__(self):
        self.urls = []
        self.used_urls = []
        self.polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
        self.english_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
        self.source = 'https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites'
    
    def scrape_urls(self):
        html_text = requests.get(self.source).text
        soup = BeautifulSoup(html_text, 'lxml')
        divs = soup.find_all('div', class_='table-responsive')
        for d in divs:
            trs = d.find_all('tr')
            for t in trs:
                link = t.find('a')
                if link and link.get('href'):
                    url = link.get('href')
                    self.urls.append(url)
    
    def replace_chars(self):
        # if 'l' is not in the url, delete the url from the list
        for i in self.urls[:]:
            if 'l' not in i:
                self.urls.remove(i)

        # for each url, replace 'l' with 'ł'
        for i in range(len(self.urls)):
            self.urls[i] = self.urls[i].replace('l', 'ł')
        
    def check_urls(self):
        # for each url get online status
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
    
    def run(self):
        self.scrape_urls()
        self.replace_chars()
        self.check_urls()

        if len(self.used_urls) == 0:
            print(self.used_urls)
            print("NO URLS IN USE!")
        else:
            print(self.used_urls)

checker = WebsiteCheckerPolishMini()
checker.run()