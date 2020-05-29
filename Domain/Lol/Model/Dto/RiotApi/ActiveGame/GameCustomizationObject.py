class GameCustomizationObject:
    def __init__(self, apiData):
        self.category      = apiData.get("category", None)
        self.content       = apiData.get("content", None)
