from Ressources.Metaclass.Singleton import Singleton
import json

class RessourcesManager(metaclass = Singleton):
    
    def __init__(self):
        self.queues = self.importQueues()

    def importQueues(self):
        filename = "Ressources/Json/queues.json"

        if filename:
            with open(filename, 'r') as f:
                datastore = json.load(f)
                return datastore
