from Domain.Lol.Model.Commands.Command import Command


class CmdKdaCs(Command):

    def __init__(self, lastMatches):
        self._lastMatches = lastMatches

    def run(self):
        kills, assists, deaths, cs, meanCs = 0, 0, 0, 0, 0

        
