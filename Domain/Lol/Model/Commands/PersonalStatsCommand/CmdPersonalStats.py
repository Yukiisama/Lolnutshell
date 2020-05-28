from abc import abstractmethod

from Domain.Lol.Model.Commands.Command import Command
from Domain.Lol.Model.Dto.RiotApi.MatchDto import MatchDto
from Domain.Lol.Model.Dto.RiotApi.MatchListDto import MatchListDto
from Domain.Lol.Model.Dto.RiotApi.MatchReferenceDto import MatchReferenceDto


class CmdPersonalStats(Command):
    # shared with others cmdPersonalStats to not recalculate match.
    _dictMatch = dict()

    def __init__(self, nbMatch, nbDays, name, mode, history, championId, lastMatches):
        self._nbMatch     = nbMatch
        self._nbDays      = nbDays
        self._name        = name
        self._mode        = mode
        self._history     = history
        self._championId  = championId
        self._lastMatchs  = lastMatches


    @abstractmethod
    def run(self):
        pass

    def getLastMatchs(self) -> MatchListDto:
        return self._lastMatchs

    def getMatchDto(self, matchRef: MatchReferenceDto) -> MatchDto:
        if CmdPersonalStats._dictMatch.get(matchRef.gameId) is None:
            CmdPersonalStats._dictMatch[matchRef.gameId] = self._history.getMatchByReference(matchRef)
        return CmdPersonalStats._dictMatch[matchRef.gameId]

    def validNbMatch(self):
        return self._nbMatch is not None and self._nbMatch != 0

    def getIDandTeam(self, match: MatchDto):
        myID = match.getParticipantIDFromAccountID(self._history.getAccountID())
        myTeam = match.getTeamIdFromParticipantId(myID)
        return myID, myTeam
