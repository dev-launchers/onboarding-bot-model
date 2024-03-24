from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import save

def protocol_from(url):
    return urlparse(url).scheme + '://'

def domain_from(url):
    return urlparse(url).netloc

def hostname_from(url):
    return urlparse(url).scheme + '://' + urlparse(url).netloc

def path_from(url):
    parsed = urlparse(url)

    # extract domain 
    domain = parsed.netloc if parsed.netloc else parsed.path
    if domain.startswith("www."):
        domain = domain[4:]

    # extract path
    path = "/".join(parsed.path.split('/')[:-1])
    
    return domain + path

def filename_from(url):
    # extract filename
    filename = urlparse(url).path.split('/')[-1]

    # complete index
    if filename == '':
        filename = 'index'

    # complet with extention
    if '.' not in filename:
        filename += '.html'

    return filename

def urls_from(response):
    url = response.url
    if url.endswith('/'):
        url = url[:-1]

    urls = set()

    # Check if request done
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Browse anchors 
        for link in soup.find_all('a'):
            href = link.get('href')
            
            # Check if link is valid, not empty, and does not contain '?' or ':'
            if href and href != '#' and not href.startswith('http') and '?' not in href and ':' not in href:
                urls.add(hostname_from(url) + href)

    else:
        print(response.status_code, ": ", url)
    
    return urls

def website_from(homepage= "https://devlaunchers.org/", iterative_limit= 4):
    ## Init
    urls = set()
    urls_browsed = set()

    urls.update({homepage})

    for i in range(iterative_limit):
        print(f'Iteration No. {i+1}')
        temporary_urls = urls.copy()

        for url in urls:
            if url not in urls_browsed:
                try:
                    # Request
                    response = requests.get(url)

                    # Go to except if the file is not an html file
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Save file
                    save.request_at(path= path_from(response.url),
                            filename= filename_from(response.url),
                            response= response)
                    
                    # To avoid duplicates
                    urls_browsed.update({response.url}) 

                    # Add the discovered urls without adding it to the current reading list
                    temporary_urls.update(urls_from(response)) 
                except:
                    # To avoid duplicates
                    urls_browsed.update({url}) 

        # Add the discovered urls
        urls = temporary_urls.copy()