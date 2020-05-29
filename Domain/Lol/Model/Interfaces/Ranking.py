from abc import ABC, abstractmethod


class Ranking(ABC):

    @abstractmethod
    def getRankBySummoner(self):
        pass
