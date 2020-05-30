from Domain.Lol.Model.Commands.PersonalStatsCommand.CmdPersonalStats import CmdPersonalStats
from Domain.Lol.Model.Dto.Stats.KdaCs import KdaCs
from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager
import datetime
import copy

class CmdKdaCs(CmdPersonalStats):

    def __init__(self, nbMatch, nbDays, name, mode, history, championId, lastMatches):
        super().__init__(nbMatch, nbDays, name, mode, history, championId, lastMatches)

    def run(self):
        # Kills, Assists, Deaths, Cs, nbGames, time, cs By Min by Champ
        dictKdaCs     = dict()

        # meanKills, meanAssists, meanDeaths, meanCs, nbGames, time
        dictMeanKdaCs = dict()

        lastMatches   = self.getLastMatchs()
        for m in lastMatches.matches:
            match        = self.getMatchDto(m)
            myID, myTeam = self.getIDandTeam(match)
            champion     = RessourcesManager().getChampionbyID(match.participants[myID - 1].championId)
            myStats      = match.participants[myID - 1].stats

            if champion not in dictKdaCs:
                dictKdaCs[champion] = [myStats.kills, myStats.assists, myStats.deaths, myStats.totalMinionsKilled, 1, match.gameDuration, 0]
            else:
                dictKdaCs[champion][0] += myStats.kills
                dictKdaCs[champion][1] += myStats.assists
                dictKdaCs[champion][2] += myStats.deaths
                dictKdaCs[champion][3] += myStats.totalMinionsKilled
                dictKdaCs[champion][4] += 1
                dictKdaCs[champion][5] += match.gameDuration
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

        # calculate cs by min by champ
        totalTime = 0
        for champion in dictKdaCs:
            dictKdaCs[champion][6]     += dictKdaCs[champion][3] / (dictKdaCs[champion][5] / 60)
            # same result (deepcopy)
            dictMeanKdaCs[champion][6]  = dictKdaCs[champion][6]
            totalTime                  += dictKdaCs[champion][5]

        minutes = totalTime / 60
        print(minutes)
        # Finally convert in format h:min:sec
        totalTime = str(datetime.timedelta(seconds=totalTime))
        for champion in dictKdaCs:
            dictKdaCs[champion][5] = str(datetime.timedelta(seconds=dictKdaCs[champion][5]))
            # same result (deepcopy)
            dictMeanKdaCs[champion][5] = dictKdaCs[champion][5]

        return KdaCs(globalKda, globalCs, meanGlobalKda, meanGlobalCs, dictKdaCs,
                     dictMeanKdaCs, globalCs / minutes, totalTime)




