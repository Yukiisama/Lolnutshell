from riotwatcher import LolWatcher

from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager
from Infrastructure.Lol.Mediator import Mediator

# You must define your own config file with key_riot.
API_KEY     = RessourcesManager().config['key_riot']
LOL_WATCHER = LolWatcher(API_KEY)
MEDIATOR    = Mediator(LOL_WATCHER)


def main():
    print("LolNutshell v0.0")
    # do stuff ...
    #MEDIATOR.showLastMatch("yukíi")
    #MEDIATOR.winRate(20,0,"yukíi", None)
    MEDIATOR.KdaCs(20,0,"yukíi", None)
    print("Bye")
    

main()
