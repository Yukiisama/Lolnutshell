from Domain.Lol.Model.Dto.RiotApi.ParticipantStatsDto import ParticipantStatsDto
from Domain.Lol.Model.Dto.RiotApi.ParticipantTimeLineDto import ParticipantTimeLineDto

class ParticipantDto():
    def __init__(self, apiData):
        self.championId                = apiData.get('championId', None)
        self.teamId                    = apiData.get('teamId', None) 
        
        self.runes                     = ([RunetDto(apiData['runes'][i]) 
                                        for i in range(len(apiData['runes']))] 
                                        if 'runes' in apiData.keys() else None)   
        
        self.masteries                 = ([RunetDto(apiData['masteries'][i]) 
                                        for i in range(len(apiData['runes']))]
                                        if 'masteries' in apiData.keys() else None)  
        
        self.highestAchievedSeasonTier = apiData.get('highestAchievedSeasonTier', None)
        
        self.timeline                  = ParticipantTimeLineDto(apiData['timeline']) if 'timeline' in apiData.keys() else None
                                        
        self.participantId             = apiData.get('participantId', None)
        
        self.stats                     = ParticipantStatsDto(apiData['stats']) if 'stats' in apiData.keys() else None
        
        self.spell2Id                  = apiData.get('spell2Id', None)
        self.spell1Id                  = apiData.get('spell1Id', None)
    
    def print(self):
        print("**Participant {} **".format(self.participantId))
        print("     championId: ", self.championId)
        print("     teamId : ", self.teamId )
        
        print("     timeline: ")
        self.timeline.print()
        
        print("     participantId: ", self.participantId)
        print("     spell2Id: ", self.spell2Id)
        print("     spell1Id: ", self.spell1Id)
        print("     runes: ", self.runes)
        print("     masteries: ", self.masteries)
        print("     highestAchievedSeasonTier: ", self.highestAchievedSeasonTier)
        
        print("     stats: ")
        self.stats.print()
        