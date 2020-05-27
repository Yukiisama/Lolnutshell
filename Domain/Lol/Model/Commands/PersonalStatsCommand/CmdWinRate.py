from Domain.Lol.Model.Commands.Command import Command
from Domain.Lol.Model.Dto.RiotApi.MatchDto import MatchDto
from Domain.Lol.Model.Dto.RiotApi.MatchListDto import MatchListDto
from Domain.Lol.Model.Dto.RiotApi.MatchReferenceDto import MatchReferenceDto
from Domain.Lol.Model.Dto.Stats.WinRate import WinRate
from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager

WIN = "Win"


class CmdWinRate(Command):

    def __init__(self, nbMatch, nbDays, name, mode, history, championId):
        self._nbMatch     = nbMatch
        self._nbDays      = nbDays
        self._name        = name
        self._mode        = mode
        self._history     = history
        self._championId  = championId
        self._lastMatchs  = None
        self._dictMatch   = dict()

    def run(self):
        if self.__validNbMatch():
            globalWinRate        = self.__globalWinRate()
            championsWinRateDict = self.__championWinRates()
            return WinRate(globalWinRate, championsWinRateDict, self._nbDays)
        return None

    def __globalWinRate(self):
        lastMatches = self.getLastMatchs()
        wins = 0
        for m in lastMatches.matches:
            match = self.getMatchDto(m)
            myID, myTeam = self.getIDandTeam(match)
            for team in match.teams:
                if team.teamId == myTeam and team.win == WIN:
                    wins += 1
        return (wins / self._nbMatch) * 100

    def __championWinRates(self):

        # [champion][win][loose][nbgame][winRate]
        dictChampionWinRate = dict()
        lastMatches = self.getLastMatchs()

        for m in lastMatches.matches:
            match        = self.getMatchDto(m)
            myID, myTeam = self.getIDandTeam(match)
            champion     = RessourcesManager().getChampionbyID(match.participants[myID - 1].championId)

            for team in match.teams:
                if team.teamId == myTeam and team.win == WIN:
                    if champion in dictChampionWinRate:
                        dictChampionWinRate[champion][0] += 1
                    else:
                        dictChampionWinRate[champion] = [1, 0, 0, 0]
                    dictChampionWinRate[champion][2] += 1
                elif team.teamId == myTeam and team.win != WIN:
                    if champion in dictChampionWinRate:
                        dictChampionWinRate[champion][1] += 1
                    else:
                        dictChampionWinRate[champion] = [0, 1, 0, 0]
                    dictChampionWinRate[champion][2] += 1

        # Simply add WinRate for each champion
        for champion in dictChampionWinRate:
            wins = dictChampionWinRate[champion][0]
            games = dictChampionWinRate[champion][2]
            if games != 0:
                dictChampionWinRate[champion][3] = (wins / games) * 100

        # Finally sorted it in order of games
        dictChampionWinRate = dict(sorted(
                                    dictChampionWinRate.items(),
                                    reverse=True,
                                    key=lambda wl: wl[1][2]
                                    ))
        return dictChampionWinRate


    def getLastMatchs(self) -> MatchListDto:
        if self._lastMatchs is None:
            self._lastMatchs = self._history.getLastMatchs(self._nbMatch, self._mode)
        return self._lastMatchs

    def getMatchDto(self, matchRef: MatchReferenceDto) -> MatchDto:
        if self._dictMatch.get(matchRef) is None:
            self._dictMatch[matchRef] = self._history.getMatchByReference(matchRef)
        return self._dictMatch[matchRef]

    def __validNbMatch(self):
        return self._nbMatch is not None and self._nbMatch != 0

    def getIDandTeam(self, match: MatchDto):
        myID = match.getParticipantIDFromAccountID(self._history.getAccountID())
        myTeam = match.getTeamIdFromParticipantId(myID)
        return myID, myTeam


