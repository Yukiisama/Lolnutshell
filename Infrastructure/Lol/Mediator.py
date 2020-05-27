from Domain.Lol.Model.Commands.PersonalStatsCommand.CmdWinRate import CmdWinRate
from Domain.Lol.Model.Dto.RiotApi.SummonerDto import SummonerDto
from Domain.Lol.Model.Interfaces.IMediator import IMediator
from Infrastructure.Lol.RiotWatcherHistory import RiotWatcherHistory


class Mediator(IMediator):

    def __init__(self, lolWatcher):
        self._lolWatcher = lolWatcher

    def winRate(self, nbMatches, nbDays, name, mode, championId=None):
        cmd = CmdWinRate(nbMatches,
                         nbDays,
                         name,
                         mode,
                         self.getRiotWatcherHistory(name),
                         championId
                         )
        winRate = cmd.run()
        winRate.print()
        return winRate

    def showLastMatch(self, name):
        history = self.getRiotWatcherHistory(name)
        matchRef = history.getLastMatch()
        history.getMatchByReference(matchRef).print()

    def getRiotWatcherHistory(self, name):
        location = 'euw1'
        profile = SummonerDto(self._lolWatcher.summoner.by_name(location, name))
        return RiotWatcherHistory(profile, location, self._lolWatcher)
