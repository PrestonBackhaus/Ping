import requests
from bs4 import BeautifulSoup

urls = []

used_urls = []

source = 'https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites'   # website for urls
html_text = requests.get(source).text   # get html text
soup = BeautifulSoup(html_text, 'lxml')  # create soup object, don't know what 'lxml' does but is necessary
divs = soup.find_all('div', class_='table-responsive')  # find all divs which contain the companies
for d in divs:
    trs = d.find_all('tr')   # find all table rows, each contains a link
    for t in trs:
        link = t.find('a')  # find the link itself which is stored in 'a' tag
        if link and link.get('href'): # if link is valid and not None
            url = link.get('href')  # get the link itself
            urls.append(url) # add it to the list of urls

# shows urls are being added, not needed
print(urls)

# if 'l' is not in the url, delete the url from the list
for i in urls[:]:
    if 'l' not in i:
        urls.remove(i)

# for each url, reaplce l with ł
for i in range(len(urls)):
    urls[i] = urls[i].replace('l', 'ł')

# for each url get online status
for i in range(len(urls)):
    try:
        response = requests.get(urls[i])
        if response.status_code == 200:     #if online, print online
            print(f"{urls[i]} is already online.\n\n")
            used_urls.append(url[i])
        else:
            print(f"{urls[i]} is offline. \n\n")        # if offline but in use, print offline
            used_urls.append(url[i])
    except requests.exceptions.RequestException as e:       # if url invalid/error
        print(f"{urls[i]} is offline or not in use: {e}")       # print not in use or error
        print("URL INVALID\n\n")

if len(used_urls) == 0:
    print(used_urls)
    print("NO URLS IN USE!")
else:
    print(used_urls)