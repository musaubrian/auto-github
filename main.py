#!/usr/bin/env python3
"""script uses github's api to create repos from terminal"""


import argparse
import json
import os
from pathlib import Path
import subprocess

from github import Github
import requests


"""global vars"""
home_path = Path.home()
to_conf = os.path.join(home_path, ".config")
full_path = Path(to_conf, ".gh_config")

with open(full_path, "r") as file:
    username = file.readlines()[0].strip()

with open(full_path, "r") as file:
    token = file.readlines()[1].strip()

with open(full_path, "r") as file:
    clone_option = file.readlines()[2].strip()

base_url = "https://api.github.com/user/repos"
auth_headers = {"Authorization": f"token {token}"}
g = Github(token)


def create_repo(
        repo_name: str,
        url: str,
        headers: dict[str, str],
        github_username: str
        ):
    """
    creates a repo with description
    adds README and gitignore
    ---
    Args:
        repo_name - name of the repositiory
        url - the base url
        headers - authentication headers
        github_username - github username
    """

    repo_desc = input("Add repo description: ")
    private_or_public = input("Make it private([Y]/n)? ")
    make_private = True
    if private_or_public == "n":
        make_private = False

    repo_info = {
            "name": repo_name,
            "description": repo_desc,
            "private": make_private
            }

    requests.post(url, headers=headers, data=json.dumps(repo_info))

    repo = g.get_user(github_username).get_repo(name=repo_name)
    repo.create_file(
            "README.md",
            "chore: initial commit",
            f"# {repo_name}\n> {repo_desc}"
    )
    print(f"========== successfully created {repo_name} ==========\n")


def list_issues(issue_state):
    """
    displays issues in select repo
    ---
    args::
        issue_state:
        open - open issues
        closed - closed issues
        all - displays all issues
    """
    repo_name = input("Repo to search issues: ")
    repo_func = g.get_user(username).get_repo(repo_name)
    issues_list = repo_func.get_issues(state=issue_state)
    print()

    if issues_list.totalCount == 0:
        print(
                f"No issues of the state [{issue_state}]",
                f"in [{repo_name}] found"
            )
    else:
        for issue in issues_list:
            print(issue)


def clone_repo(repo):
    """
    clones the created repo locally

    args:
        repo - name of the repo
    """

    alt_repo_name = input("Clone repo as? (optional): ")

    if len(alt_repo_name) < 1:
        alt_repo_name = repo

    to_personal = os.path.join(home_path, "personal")
    os.chdir(to_personal)
    if clone_option == "ssh":
        subprocess.run(
            [
                "git",
                "clone",
                f"git@github.com:{username}/{repo}",
                alt_repo_name
            ]
        )
        print("\n========== Process complete ==========")
    elif clone_option == "https":
        subprocess.run(
            [
                "git",
                "clone",
                f"https://{token}@github.com:{username}/{repo}",
                alt_repo_name,
            ]
        )
        print("\n========== Process complete ==========")
    else:
        print(f"option {clone_option} is not valid")


def handle_args():
    """hadle arguments passed"""

    parser = argparse.ArgumentParser(
        description="""
            creates a repo on github with README
            """
    )
    parser.add_argument(
        "-r",
        "--repo",
        type=str,
        help=""" Name of the github repositiory """
    )
    parser.add_argument(
        "-i",
        "--issue",
        type=str,
        help="""
            get issues using issue state [open | closed | all]
            """,
    )

    args = parser.parse_args()

    issue_options = ["open", "closed", "all"]
    state = args.issue
    repo = args.repo

    if repo is None:
        if state is None:
            raise parser.error(message="You need to parse in arguments")
        elif state in issue_options:
            print(f"issues state: {state}")
            list_issues(issue_state=state)
        elif state not in issue_options:
            print(
                f"\narg [{state}] is not a valid argument\n",
                f"\nallowed args: {issue_options}",
            )
        else:
            raise argparse.ArgumentError(
                    argument=state,
                    message="You need to parse arguments"
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
