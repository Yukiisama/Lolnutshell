class Observer:
    def __init__(self, apiData):
        self.encryptionKey  = apiData.get("encryptionKey", None)