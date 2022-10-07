# auto-github


Creates a basic repo with a **README** and an empty gitignore and clones the repo **all in just two lines** or **one** if you'd like
## Installation && setup

Clone the repository

```sh
$ git clone https://github.com/musaubrian/auto-github
```
### install requirements
```sh
$ cd auto-github

$ ./setup.py
```

-------

## Usage && Examples

```sh
$ ./main --help

usage: main [-h] [-r REPO] [-i ISSUE]

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
$ ./main -r repository_name
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
$ ./main -i closed
issues status: closed
Repo to search issues: auto-github

Issue(title="clone function", number=2)
Issue(title="add issue tracker", number=1)
```
----
> **Note**
> 
> Recommend generating a new personal token with only repo permission
> 
> You need an internet connection for the script to work
