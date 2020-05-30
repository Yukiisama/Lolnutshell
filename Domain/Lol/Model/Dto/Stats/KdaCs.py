class KdaCs:

    def __init__(self, globalKda, globalCs, meanGlobalKda, meanGlobalCs, dictKdaCs, dictMeanKdaCs, csByMin, totalTime):
        self.globalKda     = globalKda
        self.globalCs      = globalCs
        self.meanGlobalKda = meanGlobalKda
        self.meanGlobalCs  = meanGlobalCs
        self.dictKdaCs     = dictKdaCs
        self.dictMeanKdaCs = dictMeanKdaCs
        self.csByMin       = csByMin
        self.totalTime     = totalTime

    def print(self):
        print("Global Kda", self.globalKda)
        print("Global Cs", self.globalCs)
        print("Mean Global Kda", self.meanGlobalKda)
        print("Mean Global Cs", self.meanGlobalCs)
        print("Dict KdaCs : kills, assists, deaths, cs, nbGames")
        print("Cs by Min ", self.csByMin)
        print("Total time ", self.totalTime)
        for champion in self.dictKdaCs:
            print(" {} : {} ".format(champion, self.dictKdaCs[champion]))

        print("Dict MeanKdaCs : Meankills, Meanassists, Meandeaths, Meancs, nbGames")
        for champion in self.dictMeanKdaCs:
            print(" {} : {} ".format(champion, self.dictMeanKdaCs[champion]))
