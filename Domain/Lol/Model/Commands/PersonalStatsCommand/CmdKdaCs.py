from Domain.Lol.Model.Commands.PersonalStatsCommand.CmdPersonalStats import CmdPersonalStats
from Domain.Lol.Model.Dto.Stats.KdaCs import KdaCs
from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager
import copy

class CmdKdaCs(CmdPersonalStats):

    def __init__(self, nbMatch, nbDays, name, mode, history, championId, lastMatches):
        super().__init__(nbMatch, nbDays, name, mode, history, championId, lastMatches)

    def run(self):
        # Kills, Assists, Deaths, Cs, nbGames
        dictKdaCs     = dict()

        # meanKills, meanAssists, meanDeaths, meanCs, nbGames
        dictMeanKdaCs = dict()

        lastMatches   = self.getLastMatchs()
        for m in lastMatches.matches:
            match        = self.getMatchDto(m)
            myID, myTeam = self.getIDandTeam(match)
            champion     = RessourcesManager().getChampionbyID(match.participants[myID - 1].championId)
            myStats      = match.participants[myID - 1].stats

            if champion not in dictKdaCs:
                dictKdaCs[champion] = [myStats.kills, myStats.assists, myStats.deaths, myStats.totalMinionsKilled, 1]
            else:
                dictKdaCs[champion][0] += myStats.kills
                dictKdaCs[champion][1] += myStats.assists
                dictKdaCs[champion][2] += myStats.deaths
                dictKdaCs[champion][3] += myStats.totalMinionsKilled
                dictKdaCs[champion][4] += 1

        dictMeanKdaCs = copy.deepcopy(dictKdaCs)
        kdaList = [0, 0, 0, 0]
        for champion in dictMeanKdaCs:
            for i in range(4):
                dictMeanKdaCs[champion][i] /= dictMeanKdaCs[champion][4]

        globalKda     = [0, 0, 0]
        globalCs      = 0
        meanGlobalKda = [0, 0, 0]
        meanGlobalCs  = 0

        for champion in dictKdaCs:
            for i in range(3):
                globalKda[i]     += dictKdaCs[champion][i]
            globalCs     += dictKdaCs[champion][3]

        meanGlobalCs = globalCs / self._nbMatch
        for i in range(3):
            meanGlobalKda[i]  = globalKda[i] / self._nbMatch

        return KdaCs(globalKda, globalCs, meanGlobalKda, meanGlobalCs, dictKdaCs, dictMeanKdaCs)


