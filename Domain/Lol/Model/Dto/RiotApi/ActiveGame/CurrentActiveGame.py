from Domain.Lol.Model.Dto.RiotApi.ActiveGame.BannedChampion import BannedChampion
from Domain.Lol.Model.Dto.RiotApi.ActiveGame.CurrentGameParticipant import CurrentGameParticipant
from Domain.Lol.Model.Dto.RiotApi.ActiveGame.Observer import Observer


class CurrentActiveGame:
    def __init__(self, apiData):
        self.gameId            = apiData.get("gameId", None)
        self.gameType          = apiData.get("gameType", None)
        self.gameStartTime     = apiData.get("gameStartTime", None)
        self.mapId             = apiData.get("mapId", None)
        self.gameLength        = apiData.get("gameLength", None)
        self.platformId        = apiData.get("platformId", None)
        self.gameMode          = apiData.get("gameMode", None)
        self.bannedChampions   = ([BannedChampion(apiData["bannedChampions"][i])
                                 for i in range(len(apiData["bannedChampions"]))]
                                 if "bannedChampions" in apiData.keys() else None)
        self.gameQueueConfigId = apiData.get("gameQueueConfigId", None)
        self.observers         = Observer(apiData.get("observers", None))
        self.participants      = ([CurrentGameParticipant(apiData["participants"][i])
                                 for i in range(len(apiData["participants"]))]
                                 if "participants" in apiData.keys() else None)