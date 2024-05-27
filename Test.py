import requests

# Replace these with your own values
GITHUB_TOKEN = ''
REPO_OWNER = 'juveria1340'
REPO_NAME = 'Web_Scraping'

# GitHub API URL for pull requests
url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls'

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

# Send GET request to GitHub API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    pull_requests = response.json()
    num_pull_requests = len(pull_requests)
    print(f'Number of open pull requests: {num_pull_requests}')
else:
    print(f'Failed to fetch pull requests. Status code: {response.status_code}')
    print(response.json())
