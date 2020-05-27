class WinRate:

    def __init__(self, globalWinRate, championDictWinRate, days):
        self.globalWinRate       = globalWinRate
        self.championDictWinRate = championDictWinRate
        self.days                = days

    def print(self):
        print("GlobalWinRate     : ", self.globalWinRate)
        print("championsWinRates : ", self.championDictWinRate)
        print("Days : ", self.days)