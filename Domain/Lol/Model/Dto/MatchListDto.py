from Domain.Lol.Model.Dto.MatchReferenceDto import MatchReferenceDto

class MatchListDto():
    
    def __init__(self, apiData):
        self.matches    = ([MatchReferenceDto(apiData['matches'][i])
                            for i in range(len(apiData['matches']))]
		                    if 'matches' in apiData.keys() else None)
        
        self.totalGames = apiData.get("totalGames", None)
        self.startIndex = apiData.get("startIndex", None)
        self.endIndex   = apiData.get("endIndex", None)
    
    def print(self):
        print('matches')
        i = 0
        for match in self.matches:
            print("Match ", i)
            match.print()
        print('totalGames', self.totalGames)
        print('startIndex', self.startIndex)
        print('endIndex', self.endIndex)