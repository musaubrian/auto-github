# auto-github


Creates a basic repo with a README and an empty gitignore and clones the repo **all in just one line**
## Installation && setup

Clone the repository and install requirements

```sh
git clone https://github.com/musaubrian/auto-github

cd auto-github

pip install -r requirements.txt
```

### setup
create file `token` with the format:

![token-format](https://user-images.githubusercontent.com/94367979/181854680-6593e3d1-e581-4e20-bd74-f5045910a226.png)

    
## Usage && Examples

```sh
$ python3 main.py --help

usage: main.py [-h] [-r REPO] [-i ISSUE]

creates repo on github with README && gitignore

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Name of the github repositiory
  -i ISSUE, --issue ISSUE 
                        get issues using issue status [open |
                        closed | all]
```
### Example

**Repositroy arg (-r | --repo)**
```sh
$ python3 main.py -r repository_name
Add repo description: description of the repo
<Response [201]>
========== successfully created repository_name ==========

Cloning into 'repository_name'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), 463 bytes | 33.00 KiB/s, done.

========== Process complete ==========
```

**Issues arg (-i | --issue)**
```sh
$ python3 main.py -i closed
issues status: closed
Repo to search issues: auto-github

Issue(title="clone function", number=2)
Issue(title="add issue tracker", number=1)
```
## ps

You need an internet connection to use the script
