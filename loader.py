loader_version = "v2.0.0"
import urllib.request
import requests
import json
import os

def get_version():
    return loader_version

def load_update_info():
    filename = "update-infos"
    try:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/RPG-Forge-Engine/refs/heads/main/updates/"
        url = base_url + filename + ".json"
        pfad = os.path.join(os.path.dirname(__file__), "updates", "info.json")
        urllib.request.urlretrieve(url, pfad)
        with open(pfad, "r", encoding="utf-8") as f:
            update_info = json.load(f)        
        return True, update_info
    except Exception as e:
        return False, e


def download_gamefile(filename):
    try:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/RPG-Forge-Engine/refs/heads/main/gamefiles/"
        url = base_url + filename + ".json"
        pfad = os.path.join(os.path.dirname(__file__), "gamefiles", "gamefile.json")
        urllib.request.urlretrieve(url, pfad)
        return True, "Download erfolgreich"
    except Exception as e:
        return False, e

def load_gamefile():
    pfad = os.path.join(os.path.dirname(__file__), "gamefiles", "gamefile.json")
    if not os.path.exists(pfad):
        return None
    with open(pfad, "r", encoding="utf-8") as f:
        return json.load(f)

def check_gamelist():
    files = []
    try:
        api_url = "https://api.github.com/repos/Emil-das-rosa-Einhorn/RPG-Forge-Engine/contents/gamefiles"
        response = requests.get(api_url)
        if response.status_code == 200:
            items = response.json()
            for item in items:
                item_version = item.get("name").removesuffix(".json")
                files.append(item_version)
        else:
            print(f"Fehler beim Abrufen: {response.status_code}")
        return files
    except Exception as e:
        files = ["could not connect to the github page"]
        return files

def load_info ():
    game_list = check_gamelist()
    game_infos = []
    game_version = []
    try:
        for filename in game_list:
            base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/RPG-Forge-Engine/refs/heads/main/gamefiles/"
            url = base_url + filename + ".json"
            response = requests.get(url)
            if response.status_code == 200:
                item = response.json()
                game_infos.append(item["info"])
                game_version.append(item["version"])
        return game_infos, game_version
    except Exception as e:
        game_infos = ["could not connect to the github page"]
        game_version = ["could not connect to the github page"]
        return game_infos, game_version 
