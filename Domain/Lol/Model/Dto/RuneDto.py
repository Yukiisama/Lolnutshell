class RuneDto:
    
    def __init__(self, apiData):
        self.runeId = apiData.get('runeId', None)
        self.rank   = apiData.get('rank', None)
    
    def print(self):
        print("runeId: ", self.runeId)
        print("rank: ", self.rank)
        