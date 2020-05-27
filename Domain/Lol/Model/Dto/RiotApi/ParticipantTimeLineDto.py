class ParticipantTimeLineDto:
    
    def __init__(self, apiData):
        self.lane                       = apiData.get('lane', None)
        self.participantId              = apiData.get('participantId', None)
        self.csDiffPerMinDeltas         = apiData.get('csDiffPerMinDeltas', None)
        self.goldPerMinDeltas           = apiData.get('goldPerMinDeltas', None)
        self.creepsPerMinDeltas         = apiData.get('creepsPerMinDeltas', None)
        self.xpPerMinDeltas             = apiData.get('xpPerMinDeltas', None)
        self.role                       = apiData.get('role', None)
        self.damageTakenDiffPerMinDelta = apiData.get('damageTakenDiffPerMinDelta', None)
        self.damageTakenPerMinDeltas    = apiData.get('damageTakenPerMinDeltas', None)
    
    def print(self):
        print("         lane: ", self.lane)
        print("         participantId: ", self.participantId	)
        print("         csDiffPerMinDeltas: ", self.csDiffPerMinDeltas)
        print("         goldPerMinDeltas: ", self.goldPerMinDeltas)
        print("         creepsPerMinDeltas: ", self.creepsPerMinDeltas)
        print("         xpPerMinDeltas: ", self.xpPerMinDeltas)
        print("         role: ", self.role)
        print("         damageTakenDiffPerMinDelta: ", self.damageTakenDiffPerMinDelta)
        print("         damageTakenPerMinDeltas: ", self.damageTakenPerMinDeltas)
