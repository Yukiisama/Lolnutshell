class WinRate:

    def __init__(self, globalWinRate, championDictWinRate, days):
        self.globalWinRate       = globalWinRate
        self.championDictWinRate = championDictWinRate
        self.days                = days

    def print(self):
        print("GlobalWinRate     : ", self.globalWinRate)
        print("Champion WinRates : wins, looses, nbgames, winrate ")
        for champion in self.championDictWinRate:
            print(" {} : {} ".format(champion, self.championDictWinRate[champion]))
        print("Days : ", self.days)
