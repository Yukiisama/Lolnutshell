class TeamBansDto:

    def __init__(self, apiData):
        self.pickTurn   = apiData.get('pickTurn', None)
        self.championId = apiData.get('championId', None)
    
    def print(self):
        print("         pickTurn: ", self.pickTurn)
        print("         championId: ", self.championId)
        