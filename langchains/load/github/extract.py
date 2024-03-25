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
    


def repository_from(metadata_github):
    clone_url = metadata_github['clone_url']
    path = metadata_github['full_name']
    # Download Repository
    git.Repo.clone_from(url=clone_url, to_path= path)

    # Iterate over all files and folders in the directory
    for file in os.listdir(path):
        if file.startswith('.'):
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                os.remove(full_path)  # Remove the file
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path) # Remove the directory


def github_projects_from(organization, access_token):
    metadatas = repositories_metadata_from(organization, access_token)

    for metadata in metadatas:
        repository_from(metadata)