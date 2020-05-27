import json

import requests

from Ressources.Metaclass.Singleton import Singleton

QUEUES    = "Ressources/Json/queues.json"
CONFIG    = "Ressources/Json/config.json"
VERSION   = "https://ddragon.leagueoflegends.com/api/versions.json"
CHAMPION  = "http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json"
class RessourcesManager(metaclass = Singleton):

    def __init__(self):
        self.queues    = self.importJson(QUEUES)
        self.config    = self.importJson(CONFIG)
        self.champions = self.importChampion()

    def importJson(self, filename):
        if filename:
            with open(filename, 'r') as f:
                datastore = json.load(f)
                return datastore
    def importChampion(self):
        version = requests.get(VERSION).json()[0]
        datadragon = requests.get(CHAMPION.format(version)).json()
        champions = {}
        for champion in datadragon["data"]:
            id = int(datadragon["data"][champion]["key"])
            champions[id] = champion
        return champions

    def getChampionbyID(self, id: int):
        return self.champions[id]
