import requests

# Replace 'YOUR_GITHUB_TOKEN' with a valid GitHub token
github_token = 'YOUR_GITHUB_TOKEN'
headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github.v3+json'
}
pr_url = "https://api.github.com/repos/malhotra5/test-repo/pulls/12"
pr_response = requests.get(pr_url, headers=headers)
pr_data = pr_response.json()

print("Response status code:", pr_response.status_code)
print("Response content:")
print(pr_data)

if 'head' in pr_data and 'sha' in pr_data['head']:
    data = pr_data['head']['sha']
    print("SHA:", data)
else:
    print("Unable to find 'head' or 'sha' in the response. Please check if the pull request exists and you have the necessary permissions.")
