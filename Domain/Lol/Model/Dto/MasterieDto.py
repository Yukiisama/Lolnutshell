class MasteryDto:
    
    def __init__(self, apiData):
        self.masteryId = apiData.get('masteryId', None)
        self.rank      = apiData.get('rank', None)
    
    def print(self):
        print("masteryId: ", self.masteryId)
        print("rank: ", self.rank)