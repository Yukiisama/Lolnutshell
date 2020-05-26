from Domain.Lol.Model.Dto.ParticipantDto import ParticipantDto
from Domain.Lol.Model.Dto.ParticipantIdentitiesDto import ParticipantIdentitiesDto
from Domain.Lol.Model.Dto.TeamStatsDto import TeamStatsDto


class MatchDto():

    def __init__(self, apiData):
        self.seasonId = apiData.get('seasonId', None)
        self.queueId = apiData.get('queueId', None)
        self.gameId = apiData.get('gameId', None)

        self.participantIdentities = ([ParticipantIdentitiesDto(apiData['participantIdentities'][i])
                                       for i in range(len(apiData['participantIdentities']))]
                                      if 'participantIdentities' in apiData.keys() else None)

        self.gameVersion = apiData.get('gameVersion', None)
        self.platformId = apiData.get('platformId', None)
        self.gameMode = apiData.get('gameMode', None)
        self.mapId = apiData.get('mapId', None)
        self.gameType = apiData.get('gameType', None)

        self.teams = ([TeamStatsDto(apiData['teams'][i]) for i in range(len(apiData['teams']))]
                      if 'teams' in apiData.keys() else None)

        self.participants = ([ParticipantDto(apiData['participants'][i])
                              for i in range(len(apiData['participants']))]
                             if 'participants' in apiData.keys() else None)

        self.gameDuration = apiData.get('gameDuration', None)
        self.gameCreation = apiData.get('gameCreation', None)

    def print(self, participant=None):
        print("Season ID:", self.seasonId)
        print("Queue ID:", self.queueId)
        print("Game ID:", self.gameId)
        print("ParticipantIdentities:")

        for p in self.participantIdentities:
            p.print()
            print()
        i = 0

        for team in self.teams:
            i += 1
            print("** Team  n° {} **".format(i))
            team.print()

        print("Game Version:", self.gameVersion)
        print("Platform ID:", self.platformId)
        print("Game Mode:", self.gameMode)
        print("Map ID:", self.mapId)
        print("Game Type:", self.gameType)

        if participant:
            for p in self.participants: p.print()

        print("gameDuration:", self.gameDuration)
        print("gameCreation:", self.gameCreation)

    def getParticipantIDFromAccountID(self, accountID):
        for pid in self.participantIdentities:
            if pid.player.accountId == accountID:
                return pid.participantId

    def getTeamIdFromParticipantId(self, participantId):
        for participant in self.participants:
            if participant.participantId == participantId:
                return participant.teamId
