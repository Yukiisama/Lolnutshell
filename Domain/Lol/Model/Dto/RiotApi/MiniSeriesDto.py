class MiniSeriesDto:

    def __init__(self, apiData):
        self.losses   = apiData.get("losses", None)
        self.progress = apiData.get("progress", None)
        self.target   = apiData.get("target", None)
        self.wins     = apiData.get("wins", None)

    def print(self):
        print("losses", self.losses)
        print("progress", self.progress)
        print("target", self.target)
        print("wins", self.wins)
