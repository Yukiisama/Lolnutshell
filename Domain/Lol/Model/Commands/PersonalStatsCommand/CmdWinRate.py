from Domain.Lol.Model.Commands.Command import Command
from Domain.Lol.Model.Dto.MatchDto import MatchDto
from Domain.Lol.Model.Dto.MatchListDto import MatchListDto
from Domain.Lol.Model.Dto.MatchReferenceDto import MatchReferenceDto

WIN = "Win"


class CmdWinRate(Command):

    def __init__(self, nbMatch, nbDays, name, mode, history, championId):
        self._nbMatch    = nbMatch
        self._nbDays     = nbDays
        self._name       = name
        self._mode       = mode
        self._history    = history
        self._championId = championId

    def run(self):
        if self._championId is not None and self.__validNbMatch():
            return self.__RunNbMatch(True)
        elif self.__validNbMatch():
            return self.__RunNbMatch()

    def __RunNbMatch(self, champion=False):
        lastMatches = self.getLastMatchs()
        wins = 0
        for m in lastMatches.matches:
            match = self.getMatchDto(m)
            myID = match.getParticipantIDFromAccountID(self._history.getAccountID())
            myTeam = match.getTeamIdFromParticipantId(myID)
            for team in match.teams:
                if team.teamId == myTeam and team.win == WIN:
                    if champion and match.participants[myID].championId == self._championId:
                        wins += 1
                    elif not champion:
                        wins += 1

        return (wins / self._nbMatch) * 100


    def getLastMatchs(self) -> MatchListDto:
        return self._history.getLastMatchs(self._nbMatch, self._mode)

    def getMatchDto(self, matchRef: MatchReferenceDto) -> MatchDto:
        return self._history.getMatchByReference(matchRef)

    def __validNbMatch(self):
        return self._nbMatch is not None and self._nbMatch != 0

