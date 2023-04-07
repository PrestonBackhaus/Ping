import requests
from urllib.parse import urlparse

class SingleChecker:
    def __init__(self, source_url):
        self.output = ''
        self.source_url = source_url
        self.urls = [] # initialize empty list to hold generated urls
        self.trueURLs = [] # initialize empty list to hold urls that are online
        
    def polish(self):
        # Define polish_chars, english_chars, and top-level domain list
        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
        english_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
        top = ['.com', '.org', '.net', '.gov', '.edu', '.mil', '.int', '.info',
               '.biz', '.name', '.pro', '.coop', '.mobi', '.travel', '.jobs', '.tel']
        
        # Get http and domain name from source_url
        http = self.source_url.split(':')[0]
        domain = urlparse(self.source_url).netloc
        domain = domain.replace('www.', '')
        after_domain = domain.split('.')[1]
        domain_name = domain.split('.')[0]
        
        # Replace all English characters in domain name with their Polish equivalents
        for i in range(len(polish_chars)):
            domain_name = domain_name.replace(english_chars[i], polish_chars[i])
        
        # Generate URLs for each top-level domain and add to urls list
        self.urls = [f'{http}://www.{domain_name}{t}' for t in top]
        
    def checkURL(self, url):
        # Check if URL is empty
        if url=='':
            print('URL INVALID\n\n')
            self.output = 'URL INVALID\n\n'
        else:
            try:
                # Make a GET request to the URL
                response = requests.get(url) 
                if response.status_code == 200:
                    # If the response status code is 200, the URL is online
                    print(f'{url} is already online.\n\n')
                    self.output = f'{url} is already online.\n\n'
                    self.trueURLs.append(url)
                else:
                    # If the response status code is not 200, the URL is offline
                    print(f'{url} is offline.\n\n')
                    self.output = f'{url} is offline.\n\n'
            except requests.exceptions.RequestException as e:
                # If there is an exception making the request, the URL is either offline or not in use
                print(f'{url} is offline or not in use: {e}')
                print('URL INVALID\n\n')
                self.output = f'{url} is offline or not in use: {e}\nURL INVALID'
            
    def getOutput(self):
        return self.output

    def run(self):
        # Generate URLs for each top-level domain and check if they are online or not
        self.polish()
        self.checkURL(self.source_url)
        for url in self.urls:
            self.checkURL(url)
        return self.trueURLs
    
    def test(self):
        # Test function
        url = "https://www.google.com"
        checker = SingleChecker(url)
        true_urls = checker.run()
        assert url in true_urls
        return true_urls
    
if __name__ == '__main__':
    # Run test function
    SingleChecker('').test()
