#!/usr/bin/env python3
"""script uses github's api to create repo's from terminal"""
import requests
import json
from github import Github

"""global vars"""
username = "musaubrian"
base_url = "https://api.github.com/user/repos"

with open("./token", "r") as file:
    token = file.read()

g = Github(token)
auth_headers = {"Authorization": f"token {token}"}


def create_repo():
    """creates a repo with description"""
    repo_name = input("Enter repo name: ")
    repo_desc = input("Add repo description: ")
    repo_info = {"name": repo_name, "description": repo_desc}
    response = requests.post(
            base_url,
            headers=auth_headers,
            data=json.dumps(repo_info)
            )
    print(response)
    repo = g.get_user(username).get_repo(name=repo_name)
    repo.create_file(
            ".gitignore", "add gitignore", ""
            )
    repo.create_file(
            "README.md", "add readme", f"# {repo_name}\n> {repo_desc}"
            )

if __name__ == "__main__":
    create_repo()
