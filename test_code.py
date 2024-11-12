import requests

github_token = "YOUR_GITHUB_TOKEN_HERE"  # Replace this with a valid GitHub token
headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github.v3+json'
}
pr_url = "https://api.github.com/repos/malhotra5/test-repo/pulls/12"
pr_response = requests.get(pr_url, headers=headers)
pr_data = pr_response.json()
if 'head' in pr_data:
    print(f"SHA: {pr_data['head']['sha']}")
else:
    print("Error: Unable to retrieve PR data")
    print(f"Response: {pr_data}")
