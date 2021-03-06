from Domain.Lol.Model.Dto.RiotApi.MatchDto import MatchDto
from Domain.Lol.Model.Dto.RiotApi.MatchListDto import MatchListDto
from Domain.Lol.Model.Interfaces.History import History


class RiotWatcherHistory(History):
    
    def __init__(self, summonerDto, location, lolWatcher):
        self._summonerDto = summonerDto
        self._location    = location
        self._lolWatcher  = lolWatcher
        self._accountID   = summonerDto.accountId

    def getAccountID(self):
        return "" + self._accountID

    def getMatchbyId(self, matchId):
        return MatchDto(self._lolWatcher.match.by_id(self._location, matchId))

    def getMatchByReference(self, matchReference) -> MatchDto:
        if matchReference and matchReference.gameId:
            matchId = matchReference.gameId
            return self.getMatchbyId(matchId)
        return None

    def getLastMatch(self, modeSet=None):
        match = self.getLastMatchs(1, modeSet) 
        if match.matches:
            return match.matches[0]
        return None 
    
    def getLastMatchs(self, nbMatches, modeSet = None, championId=None) -> MatchListDto:
        return self.getMatchs(modeSet, None, None, 0, nbMatches, None, championId)
    
    def getMatchs(self, modeSet, timeStart, timeEnd, indexStart, indexEnd, seasonSet, championSet):
        matchList = MatchListDto(self._lolWatcher.match.matchlist_by_account
                (
                    self._location,
                    self._summonerDto.accountId,
                    modeSet,
                    timeStart,
                    timeEnd,
                    indexStart,
                    indexEnd,
                    seasonSet,
                    championSet
                ))
        
        return matchList
        
    def getTimeLine(self, matchId):
        raise NotImplementedError