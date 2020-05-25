class MatchReferenceDto:
    
    def __init__(self, apiData):
        self.lane       =  apiData.get("lane", None)
        self.gameId     =  apiData.get("gameId", None)
        self.champion   =  apiData.get("champion", None)
        self.platformId =  apiData.get("platformId", None)
        self.season     =  apiData.get("season", None)
        self.queue      =  apiData.get("queue", None)
        self.role       =  apiData.get("role", None)
        self.timestamp  =  apiData.get("timestamp", None)
        
    def print(self):
        print('     lane', self.lane)
        print('     gameId', self.gameId)
        print('     champion', self.champion)
        print('     platformId', self.platformId)
        print('     season', self.season)
        print('     queue', self.queue)
        print('     role', self.role)
        print('     timestamp', self.timestamp)