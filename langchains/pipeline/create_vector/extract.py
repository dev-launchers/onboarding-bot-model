import os
import shutil
import requests
import git

def repositories_metadata_from(organization, access_token):
    params = {
        'sort': 'updated',
        'direction': 'desc',
        'per_page': 100
    }

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/orgs/{organization}/repos'

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f'Error {response.status_code}: Unable to retrieve organization repositories.')
        return None
    

def remove_hidden_at(path):    
    # Iterate over all files and folders in the directory
    for file in os.listdir(path):
        if file.startswith('.'):
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                os.remove(full_path)  # Remove the file
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path) # Remove the directory


def repository_from(metadata_github):
    clone_url = metadata_github['clone_url']
    path = metadata_github['full_name']
    try:
        # Download Repository
        git.Repo.clone_from(url=clone_url, to_path= path)

        remove_hidden_at(path)
    except:
        pass


def wiki_from(metadata_github):
    full_name = metadata_github['full_name']
    path = os.path.join('wiki', full_name)
    url = f"https://github.com/{full_name}.wiki.git"
    try:
        # Download Repository
        git.Repo.clone_from(url=url, to_path= path)

        remove_hidden_at(path)
    except:
        pass                


def github_projects_from(organization, access_token):
    metadatas = repositories_metadata_from(organization, access_token)

    for metadata in metadatas:
        repository_from(metadata)


def github_wikis_from(organization, access_token):
    metadatas = repositories_metadata_from(organization, access_token)

    for metadata in metadatas:
        wiki_from(metadata)

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