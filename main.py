#!/usr/bin/env python3
"""script uses github's api to create repos from terminal"""
import requests
import json
from github import Github

"""global vars"""
with open("./token", "r") as file:
    token = file.read()

username = "musaubrian"
base_url = "https://api.github.com/user/repos"
auth_headers = {"Authorization": f"token {token}"}
g = Github(token)


def create_repo(url, headers, github_username):
    """
    creates a repo with description
    adds README and gitignore

    Args::

    url - the base url
    headers - authentication headers
    github_username - github username
    """
    repo_name = input("Enter repo name: ")
    repo_desc = input("Add repo description: ")
    repo_info = {"name": repo_name, "description": repo_desc}
    response = requests.post(
            url,
            headers=headers,
            data=json.dumps(repo_info)
            )
    print(response)
    repo = g.get_user(github_username).get_repo(name=repo_name)
    repo.create_file(
            ".gitignore", "add gitignore", ""
            )
    repo.create_file(
            "README.md", "add readme", f"# {repo_name}\n> {repo_desc}"
            )
    print(f"==========successfully created {repo_name}==========")


def issue_tracker():
    """
    displays issues in select repo
    status:
        open - open issues
        closed - closed issues
        all - displays all issues
    """
    pass


def list_repos():
    """lists all repos"""
    pass


def clone_repo():
    """clones the created repo locally"""
    pass


def handle_args():
    """hadle arguments passed"""
    pass


if __name__ == "__main__":
    create_repo(url=base_url, headers=auth_headers, github_username=username)
