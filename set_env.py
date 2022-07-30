#!/usr/bin/env python3
"""setsup user `environment`"""

from pathlib import Path
import subprocess


def set_env():
    """
    Installs required modules
    checks if token file exists
    if false asks for required input and creates it
    """

    gh_config = Path(".gh_config")
    if gh_config.exists() is False:
        gh_username = input("Github username: ")
        gh_token = input("Github token: ")
        with open(".gh_config", "w") as file:
            file.write(f"{gh_username}\n{gh_token}")

    print("\n", "="*50, "\n")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("================Everything is set====================")


if __name__ == "__main__":
    set_env()
