from Domain.Lol.Model.Dto.RiotApi.MiniSeriesDto import MiniSeriesDto


class LeagueEntryDto:

    def __init__(self, apiData):
        self.leagueId              = apiData.get("leagueId", None)
        self.summonerId            = apiData.get("summonerId", None)
        self.summonerName          = apiData.get("summonerName", None)
        self.queueType             = apiData.get("queueType", None)
        self.tier                  = apiData.get("tier", None)
        self.rank                  = apiData.get("rank", None)
        self.leaguePoints          = apiData.get("leaguePoints",None)
        self.wins                  = apiData.get("wins", None)
        self.losses                = apiData.get("losses", None)
        self.hotStreak             = apiData.get("hotStreak", None)
        self.veteran               = apiData.get("veteran", None)
        self.freshBlood            = apiData.get("freshBlood", None)
        self.inactive              = apiData.get("inactive", None)
        self.miniSeries            = MiniSeriesDto(apiData.get("miniSeries")) if "miniSeries" in apiData else None

    def print(self):
        print("leagueId    ", self.leagueId)
        print("summonerId  ", self.summonerId)
        print("summonerName", self.summonerName)
        print("queueType   ", self.queueType)
        print("tier        ", self.tier)
        print("rank        ", self.rank)
        print("leaguePoints", self.leaguePoints)
        print("wins        ", self.wins)
        print("losses      ", self.losses)
        print("hotStreak   ", self.hotStreak)
        print("veteran     ", self.veteran)
        print("freshBlood  ", self.freshBlood)
        print("inactive    ", self.inactive)
        if self.miniSeries is not None:
            print("miniSeries  ", self.miniSeries.print())

