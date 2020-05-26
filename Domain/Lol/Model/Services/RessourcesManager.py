import json

from Ressources.Metaclass.Singleton import Singleton

QUEUES = "Ressources/Json/queues.json"
CONFIG = "Ressources/Json/config.json"

class RessourcesManager(metaclass = Singleton):

    def __init__(self):
        self.queues   = self.importJson(QUEUES)
        self.config   = self.importJson(CONFIG)

    def importJson(self, filename):
        if filename:
            with open(filename, 'r') as f:
                datastore = json.load(f)
                return datastore

