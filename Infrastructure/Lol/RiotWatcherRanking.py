from Domain.Lol.Model.Dto.RiotApi.ActiveGame.CurrentActiveGame import CurrentActiveGame
from Domain.Lol.Model.Dto.RiotApi.LeagueEntryDto import LeagueEntryDto
from Domain.Lol.Model.Interfaces.Ranking import Ranking


class RiotWatcherRanking(Ranking):

    def __init__(self, summonerDto, location, lolWatcher):
        self._summonerDto = summonerDto
        self._location    = location
        self._lolWatcher  = lolWatcher
        self._accountID   = summonerDto.accountId

    def getSummoner(self):
        return self._summonerDto

    def getRankBySummoner(self):
        data = self._lolWatcher.league.by_summoner(self._location, self._summonerDto.id)
        entries = []
        for leagueEntry in data:
            entries.append(LeagueEntryDto(leagueEntry))
        return entries

    def getActiveGame(self) -> CurrentActiveGame:
        return CurrentActiveGame(self._lolWatcher.spectator.by_summoner(self._location, self._summonerDto.id))

