#!/usr/bin/env python3
"""sets-up user `environment`"""

import os
from pathlib import Path
import subprocess


def set_env():
    """
    Installs required modules
    checks if token file exists
    if false asks for required input and creates it
    """

    home_path = Path.home()
    to_conf = os.path.join(home_path, ".config")
    full_path = Path(to_conf, ".gh_config")
    if full_path.exists() is False:
        gh_username = input("Github username: ")
        gh_token = input("Github token: ")
        clone_option = input("Use ssh or https: (https | ssh)\n")
        if clone_option == "ssh":
            print("""
-----------------------------------------------------------------------------
                    You will need to setup the ssh keys
                            learn more here ⬇️

    https://docs.github.com/en/authentication/connecting-to-github-with-ssh

-----------------------------------------------------------------------------
                  """)
        with open(full_path, "w") as file:
            file.write(f"{gh_username}\n{gh_token}\n{clone_option}")
    else:
        raise FileExistsError("File already exists")

    print("\n", "=" * 50, "\n")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("================Everything is set====================")


if __name__ == "__main__":
    set_env()
