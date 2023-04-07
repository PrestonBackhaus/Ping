import requests
from urllib.parse import urlparse

class AllChecker:
    def __init__(self, source_url):
        # Initialize instance variables
        self.output = ''
        self.source_url = source_url
        self.urls = []
        self.onlineURLs = []
        self.offlineURLs = []

    def polish(self):
        # Define polish_chars, english_chars, and top-level domain list
        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
        english_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
        top = ['.com', '.pl','.org', '.net', '.gov', '.edu', '.mil', '.int', '.info',
            '.biz', '.name', '.pro', '.coop', '.mobi', '.travel', '.jobs', '.tel']
        
        
        # Get http and domain name from source_url
        http = self.source_url.split(':')[0]
        domain = urlparse(self.source_url).netloc
        domain = domain.replace('www.', '')
        after_domain = domain.split('.')[1]
        domain_name = domain.split('.')[0]
        
        # Append source_url with all top-level domains to urls list
        for t in top:
            self.urls.append(f'{http}://www.{domain_name}{t}')

        # Check for URLs containing only a single swap of a letter
        for i in range(len(domain_name)):
            if domain_name[i] in english_chars:
                for j in range(len(polish_chars)):
                    if domain_name[i] != english_chars[j]:
                        new_domain_name = domain_name[:i] + \
                            polish_chars[j] + domain_name[i+1:]
                        if new_domain_name == domain_name:
                            continue
                        differences = sum(
                            [1 for k in range(len(domain_name)) if domain_name[k] != new_domain_name[k]])
                        if differences == 1:
                            # Append URLs with single letter swap to urls list
                            for t in top:
                                self.urls.append(
                                    f'{http}://www.{new_domain_name}{t}')


    def checkURL(self, url):
        if url == '':
            # If URL is empty, print error message
            print('URL INVALID\n\n')
            self.output = 'URL INVALID\n\n'
        else:
            try:
                # Try to get response from URL
                response = requests.get(url)
                if response.status_code == 200:
                    # If status code is 200, print URL is online
                    print(f'{url} is already online.\n\n')
                    self.output = f'{url} is already online.\n\n'
                    # Add URL to onlineURLs list
                    self.onlineURLs.append(url)
                else:
                    # If status code is not 200, print URL is offline
                    print(f'{url} is offline.\n\n')
                    self.output = f'{url} is offline.\n\n'
                    self.offlineURLs.append(url)
            except requests.exceptions.RequestException as e:
                # If request exception is caught, print error message and URL is invalid
                print(f'{url} is offline or not in use: {e}')
                print('URL INVALID\n\n')
                self.output = f'{url} is offline or not in use: {e}\nURL INVALID'

    def getOutput(self):
        # Return output variable
        return self.output

    def run(self):
        # Run polish function to append URLs to urls list
        self.polish()
        # Check source_url
        self.checkURL(self.source_url)
        # Check URLs in urls list
        for url in self.urls:
            self.checkURL(url)
        # Print onlineURLs list
        print(f'Online URLs: {self.onlineURLs}')
        # Print offlineURLs list
        print(f'Offline URLs: {self.offlineURLs}')

    def test(self):
        # Test function
        self.polish()
        print(self.urls)
    
if __name__ == '__main__':
    # Run test function
    #AllChecker('').test()
    checker = AllChecker('https://www.onet.com')
    checker.run()