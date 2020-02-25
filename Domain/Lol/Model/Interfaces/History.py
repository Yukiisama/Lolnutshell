from abc import ABC, abstractmethod

class History(ABC):
    
    @abstractmethod
    def getLastMatch(self, mode):
        pass
    
    @abstractmethod
    def getLastMatchs(self, nbMatches, mode):
        pass
    
    @abstractmethod
    def getMatchs(self, modeSet, timeStart, timeEnd, indexStart, indexEnd, seasonSet, championSet):
        pass
    
    @abstractmethod    
    def getTimeLine(self, matchId):
        pass
    