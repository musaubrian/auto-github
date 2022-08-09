import os
from pathlib import Path

def test():
    """
    test
    """
    home_path = Path.home()
    to_conf = os.path.join(home_path, ".config")
    os.chdir(to_conf)
    os.mkdir("gh")
    full_path = os.path.join(to_conf, "gh")
    print(full_path)

test()
