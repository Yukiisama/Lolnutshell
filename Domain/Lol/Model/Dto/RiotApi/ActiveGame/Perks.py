class Perks:
    def __init__(self, apiData):
        self.perkIds      = apiData.get("perkIds", None)
        self.perkStyle    = apiData.get("perkStyle", None)
        self.perkSubStyle = apiData.get("perkSubStyle", None)
