import json
import conf
import requests

from Ressources.Metaclass.Singleton import Singleton

QUEUES   = conf.ROOT_DIR + "/Ressources/Json/queues.json"
CONFIG   = conf.ROOT_DIR + "/Ressources/Json/config.json"
VERSION  = "https://ddragon.leagueoflegends.com/api/versions.json"
CHAMPION = "http://ddragon.leagueoflegends.com/cdn/10.11.1/data/en_US/champion.json"
SPELLS   = "http://ddragon.leagueoflegends.com/cdn/10.11.1/data/en_US/summoner.json"

def importDDragon(link, spells=None):
    version = requests.get(VERSION).json()[0]
    datadragon = requests.get(link.format(version)).json()
    data = {}
    for key in datadragon["data"]:
        id = int(datadragon["data"][key]["key"])
        data[id] = key if spells is None else datadragon["data"][key]["name"]
    return data


class RessourcesManager(metaclass=Singleton):
    champions = importDDragon(CHAMPION)
    spells    = importDDragon(SPELLS, True)

    def __init__(self):
        self.queues = self.importJson(QUEUES)
        self.config = self.importJson(CONFIG)

    def importJson(self, filename):
        if filename:
            with open(filename, 'r') as f:
                datastore = json.load(f)
                return datastore

    def getChampionbyID(self, id: int):
        return RessourcesManager.champions[id]

    def getSpellById(self, id: int):
        return RessourcesManager.spells[id]

    def getIconUrlById(self, id: int):
        return "http://ddragon.leagueoflegends.com/cdn/10.11.1/img/profileicon/" + str(id) +".png"

    def getChampIconUrlByName(self, name):
        return "http://ddragon.leagueoflegends.com/cdn/10.11.1/img/champion/"+ name +".png"
