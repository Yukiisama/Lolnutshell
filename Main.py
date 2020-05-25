from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager
from Domain.Lol.Model.Dto.SummonerDto            import SummonerDto
from Infrastructure.Lol.RiotWatcherHistory       import RiotWatcherHistory
from riotwatcher import RiotWatcher, ApiError 
API_KEY = "RGAPI-bd0d4c05-247b-4445-a674-2a2d17453fe2"

def main():
    print("LolNutshell v0.0")
    #do stuff ...
    print("Bye")
    a = RessourcesManager()
    lolWatcher  = RiotWatcher(API_KEY)
    location    = 'euw1'
    profile     = SummonerDto(lolWatcher.summoner.by_name(location, 'yukíi'))
    history     = RiotWatcherHistory(profile, location, lolWatcher)
    matchRef = history.getLastMatch()
    history.getMatchByReference(matchRef).print()
main()    