from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager


class BannedChampion:
    def __init__(self, apiData):
        self.pickTurn   = apiData.get("pickTurn", None)
        self.championId = apiData.get("championId", None)
        self.teamId     = apiData.get("teamId", None)

    def getChampion(self):
        return RessourcesManager().getChampionbyID(self.championId)
