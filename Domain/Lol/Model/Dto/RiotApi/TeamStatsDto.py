from Domain.Lol.Model.Dto.RiotApi.TeamBansDto import TeamBansDto

class TeamStatsDto:

    def __init__(self, apiData):
        self.firstDragon            = apiData.get("firstDragon", None)
        self.firstInhibitor         = apiData.get("firstInhibitor", None)

        self.bans                   = ([TeamBansDto(apiData['bans'][i])
                                        for i in range(len(apiData['bans']))]
                                        if 'bans' in apiData.keys() else None)

        self.baronKills             = apiData.get("baronKills", None)
        self.firstRiftHerald        = apiData.get("firstRiftHerald", None)
        self.firstBaron             = apiData.get("firstBaron", None)
        self.riftHeraldKills        = apiData.get("riftHeraldKills", None)
        self.firstBlood             = apiData.get("firstBlood", None)
        self.teamId                 = apiData.get("teamId", None)
        self.firstTower             = apiData.get("firstTower", None)
        self.vilemawKills           = apiData.get("vilemawKills", None)
        self.inhibitorKills         = apiData.get("inhibitorKills", None)
        self.towerKills             = apiData.get("towerKills", None)
        self.dominionVictoryScore   = apiData.get("dominionVictoryScore", None)
        self.win                    = apiData.get("win", None)
        self.dragonKills            = apiData.get("dragonKills", None)

    def print(self):
        print("     firstDragon: ", self.firstDragon)
        print("     firstInhibitor: ", self.firstInhibitor)
        print("     bans: ")
        
        i = 1
        for ban in self.bans:
            print("     Ban ", i)
            ban.print()
            i+=1
        
        print("     baronKills: ", self.baronKills)
        print("     firstRiftHerald: ", self.firstRiftHerald)
        print("     firstBaron: ", self.firstBaron)
        print("     riftHeraldKills: ", self.riftHeraldKills)
        print("     firstBlood: ", self.firstBlood)
        print("     teamId: ", self.teamId)
        print("     firstTower: ", self.firstTower)
        print("     vilemawKills: ", self.vilemawKills)
        print("     inhibitorKills: ", self.inhibitorKills)
        print("     towerKills: ", self.towerKills)
        print("     dominionVictoryScore: ", self.dominionVictoryScore)
        print("     win: ", self.win)
        print("     dragonKills: ", self.dragonKills)
        