from Domain.Lol.Model.Dto.RiotApi.ActiveGame.GameCustomizationObject import GameCustomizationObject
from Domain.Lol.Model.Dto.RiotApi.ActiveGame.Perks import Perks
from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager


class CurrentGameParticipant:
    def __init__(self, apiData):
        self.championId               = apiData.get("championId", None)
        self.perks                    = Perks(apiData.get("perks", None))
        self.profileIconId            = apiData.get("profileIconId", None)
        self.bot                      = apiData.get("bot", None)
        self.teamId                   = apiData.get("teamId", None)
        self.summonerName             = apiData.get("summonerName", None)
        self.summonerId               = apiData.get("summonerId", None)
        self.spell1Id                 = apiData.get("spell1Id", None)
        self.spell2Id                 = apiData.get("spell2Id", None)
        self.gameCustomizationObjects = ([GameCustomizationObject(apiData["gameCustomizationObjects"][i])
                                        for i in range(len(apiData["gameCustomizationObjects"]))]
                                        if "gameCustomizationObjects" in apiData.keys() else None)
    def getChampion(self):
        return RessourcesManager().getChampionbyID(self.championId)
