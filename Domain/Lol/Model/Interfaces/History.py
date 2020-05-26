from abc import ABC, abstractmethod

from Domain.Lol.Model.Dto import MatchListDto, MatchDto


class History(ABC):
    
    @abstractmethod
    def getLastMatch(self, mode):
        pass

    @abstractmethod
    def getAccountID(self):
        pass

    @abstractmethod
    def getMatchByReference(self, matchReference) -> MatchDto:
        pass

    @abstractmethod
    def getLastMatchs(self, nbMatches, mode) -> MatchListDto:
        pass
    
    @abstractmethod
    def getMatchs(self, modeSet, timeStart, timeEnd, indexStart, indexEnd, seasonSet, championSet):
        pass
    
    @abstractmethod    
    def getTimeLine(self, matchId):
        pass
    