from Domain.Lol.Model.Dto.RiotApi.PlayerDto import PlayerDto

class ParticipantIdentitiesDto:
    
    def __init__(self, apiData):
        self.player        = PlayerDto(apiData['player']) if 'player' in apiData.keys() else None
        self.participantId = apiData.get("participantId", None)
        
    def print(self):
        print("     player: ")
        self.player.print()
        print("     participantId", self.participantId)