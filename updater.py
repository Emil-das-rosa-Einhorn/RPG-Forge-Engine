#v1.0.0
import subprocess
import sys
import urllib.request
import requests
import json
import os

def download_loader(filename):
    try:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/RPG-Forge-Engine/refs/heads/main/"
        url = base_url + filename + ".py"
        print (url)
        pfad = os.path.join(os.path.dirname(__file__), filename + ".py")
        print (pfad)
        urllib.request.urlretrieve(url, pfad)
        return True, "Download erfolgreich"
    except Exception as e:
        return False, e

def main ():
    l_up = sys.argv[1]
    m_up = sys.argv[2]
    if l_up == "True":
        download_loader("loader")
    else:
        pass
    if m_up == "True":
        download_loader("RPG-Main")
    else:
        pass
    
    return 1

if __name__ == "__main__":
    sys.exit(main())
