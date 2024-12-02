import os
import requests

github_token = os.getenv('GITHUB_TOKEN')
headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github.v3+json'
}
pr_url = "https://api.github.com/repos/malhotra5/test-repo/pulls/12"
pr_response = requests.get(pr_url, headers=headers)
pr_data = pr_response.json()
data = pr_data['head']['sha']
print(data)
