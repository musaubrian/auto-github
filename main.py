#!/usr/bin/env python3
"""script uses github's api to create repos from terminal"""

from github import Github
import requests
import json
import argparse
import subprocess
import os


"""global vars"""

with open("gh_config", "r") as file:
    username = file.readlines()[0].strip()

with open("gh_config", "r") as file:
    token = file.readlines()[1].strip()

base_url = "https://api.github.com/user/repos"
auth_headers = {"Authorization": f"token {token}"}
g = Github(token)


def create_repo(repo_name, url, headers, github_username):
    """
    creates a repo with description
    adds README and gitignore

    Args:
        repo_name - name of the repositiory
        url - the base url
        headers - authentication headers
        github_username - github username
    """

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
    print(f"========== successfully created {repo_name} ==========\n")


def list_issues(issue_status):
    """
    displays issues in select repo

    args::
    issue_status:
        open - open issues
        closed - closed issues
        all - displays all issues
    """
    repo_name = input("Repo to search issues: ")
    repo_func = g.get_user(username).get_repo(repo_name)
    issues_list = repo_func.get_issues(state=issue_status)
    print()

    for issue in issues_list:
        print(issue)


def clone_repo(repo):
    """
    clones the created repo locally

    args:
    repo - name of the repo
    """
    os.chdir("..")
    subprocess.run(
            ["git", "clone", f"https://{token}@github.com/{username}/{repo}"]
            )
    print("\n========== Process complete ==========")


def handle_args():
    """hadle arguments passed"""

    parser = argparse.ArgumentParser(
            description="""
            creates repo on github with README && gitignore
            """)
    parser.add_argument(
            "-r", "--repo",
            type=str,
            help=""" Name of the github repositiory """
            )
    parser.add_argument(
            "-i", "--issue",
            type=str,
            help="""
            get issues using issue status [open | closed | all]
            """
            )

    args = parser.parse_args()

    issue_options = ["open", "closed", "all"]
    status = args.issue
    repo = args.repo

    if repo is None:
        if status is None:
            raise parser.error(message="You need to parse arguments")
        elif status in issue_options:
            print(f"issues status: {status}")
            list_issues(issue_status=status)
        elif status not in issue_options:
            print(
                    f"\narg [{status}] is not a vlid argument\n",
                    f"\nallowed args: [{issue_options}]"
                    )
    elif repo is not None:
        create_repo(
                repo_name=repo,
                url=base_url,
                headers=auth_headers,
                github_username=username
                )
        clone_repo(repo=repo)


if __name__ == "__main__":
    handle_args()
