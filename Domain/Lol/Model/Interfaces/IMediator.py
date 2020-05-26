from abc import ABC, abstractmethod


class IMediator(ABC):

    @abstractmethod
    def showLastMatch(self, name):
        pass

    @abstractmethod
    def winRate(self, nbMatches, nbDays, name, mode):
        pass

    @abstractmethod
    def getRiotWatcherHistory(self, name):
        pass
