class PlayerDto:
    
    def __init__(self, apiData):
        self.currentPlatformId  = apiData.get('currentPlatformId', None)
        self.summonerName       = apiData.get('summonerName', None)
        self.matchHistoryUri    = apiData.get('matchHistoryUri', None)
        self.platformId         = apiData.get('platformId', None)
        self.currentAccountId   = apiData.get('currentAccountId', None)
        self.profileIcon        = apiData.get('profileIcon', None)
        self.summonerId         = apiData.get('summonerId', None)
        self.accountId          = apiData.get('accountId', None)

    def print(self):
        print('         currentPlatformId', self.currentPlatformId)
        print('         summonerName', self.summonerName)
        print('         matchHistoryUri', self.matchHistoryUri)
        print('         platformId', self.platformId)
        print('         currentAccountId', self.currentAccountId)
        print('         profileIcon', self.profileIcon)
        print('         summonerId', self.summonerId)
        print('         accountId', self.accountId)