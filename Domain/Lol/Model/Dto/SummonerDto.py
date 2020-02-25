class SummonerDto:
    
    def __init__(self, apiData):
        self.profileIconId  = apiData.get('profileIconId', None)
        self.name           = apiData.get('name', None)
        self.puuid          = apiData.get('puuid', None)
        self.summonerLevel  = apiData.get('summonerLevel', None)
        self.revisionDate   = apiData.get('revisionDate', None)
        self.id             = apiData.get('id', None)
        self.accountId      = apiData.get('accountId', None)
    
    def print(self):
        print('profileIconId', self.profileIconId)
        print('name', self.name)
        print('puuid', self.puuid)
        print('summonerLevel', self.summonerLevel)
        print('revisionDate', self.revisionDate)
        print('id', self.id)
        print('accountId', self.accountId)
        