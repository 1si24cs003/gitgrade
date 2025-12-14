import requests

def parse_github_url(url):
    if not url.startswith("https://github.com/"):
        raise ValueError("Invalid GitHub URL")

    parts = url.rstrip("/").split("/")
    if len(parts) < 5:
        raise ValueError("Use format: https://github.com/user/repo")

    return parts[-2], parts[-1]


def analyze_repo(repo_url):
    owner, repo = parse_github_url(repo_url)

    repo_api = f"https://api.github.com/repos/{owner}/{repo}"
    commits_api = f"https://api.github.com/repos/{owner}/{repo}/commits"
    readme_api = f"https://api.github.com/repos/{owner}/{repo}/readme"

    repo_data = requests.get(repo_api).json()
    commits = requests.get(commits_api).json()
    readme_resp = requests.get(readme_api)

    return {
        "name": repo,
        "language": repo_data.get("language"),
        "stars": repo_data.get("stargazers_count", 0),
        "commit_count": len(commits) if isinstance(commits, list) else 0,
        "has_readme": readme_resp.status_code == 200
    }
