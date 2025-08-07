import requests

def task_func(user, API_URL='https://api.github.com/users/'):
    # Construct the URL to access the user's repositories
    url = f"{API_URL}{user}/repos"
    
    try:
        # Make a GET request to the GitHub API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        repos = response.json()
        
        # Extract repository names and their creation dates
        repo_info = [(repo['name'], repo['created_at']) for repo in repos]
        
        # Sort the repositories by their creation date
        sorted_repos = sorted(repo_info, key=lambda x: x[1])
        
        # Extract and return the sorted list of repository names
        return [repo[0] for repo in sorted_repos]
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
# repo_names = task_func('octocat')
# print(repo_names)