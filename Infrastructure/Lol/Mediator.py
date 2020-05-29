from Domain.Lol.Model.Commands.PersonalStatsCommand.CmdKdaCs import CmdKdaCs
from Domain.Lol.Model.Commands.PersonalStatsCommand.CmdWinRate import CmdWinRate
from Domain.Lol.Model.Dto.RiotApi.SummonerDto import SummonerDto
from Domain.Lol.Model.Interfaces.IMediator import IMediator
from Infrastructure.Lol.RiotWatcherHistory import RiotWatcherHistory
from Infrastructure.Lol.RiotWatcherRanking import RiotWatcherRanking


class Mediator(IMediator):

    def __init__(self, lolWatcher):
        self._lolWatcher  = lolWatcher
        self._historyDict = dict()

    def winRate(self, nbMatches, nbDays, name, mode=None, championId=None):
        cmd = CmdWinRate(nbMatches,
                         nbDays,
                         name,
                         mode,
                         self.getRiotWatcherHistory(name),
                         championId,
                         self.getRiotWatcherHistory(name).getLastMatchs(nbMatches, mode)
                         )
        winRate = cmd.run()
        winRate.print()
        return winRate

    def KdaCs(self, nbMatches, nbDays, name, mode=None, championId=None):
        cmd = CmdKdaCs(nbMatches,
                         nbDays,
                         name,
                         mode,
                         self.getRiotWatcherHistory(name),
                         championId,
                         self.getRiotWatcherHistory(name).getLastMatchs(nbMatches, mode)
                         )
        kdaCs = cmd.run()
        kdaCs.print()
        return kdaCs

    def showLastMatch(self, name):
        history = self.getRiotWatcherHistory(name)
        matchRef = history.getLastMatch()
        history.getMatchByReference(matchRef).print()

    def getRiotWatcherHistory(self, name):
        if not self._historyDict.get(name):
            location = 'euw1'
            profile  = SummonerDto(self._lolWatcher.summoner.by_name(location, name))
            history  = RiotWatcherHistory(profile, location, self._lolWatcher)
            self._historyDict[name] = history

        return self._historyDict[name]

    def getRiotRanking(self, name):
        location = 'euw1'
        profile  = SummonerDto(self._lolWatcher.summoner.by_name(location, name))
        ranking  = RiotWatcherRanking(profile, location, self._lolWatcher)
        return ranking
