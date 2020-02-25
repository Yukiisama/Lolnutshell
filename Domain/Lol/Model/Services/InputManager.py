class InputManager:
    
    @staticmethod
    def getInput(attribute, displayMessage = "Input your "):
        print(displayMessage, attribute)
        return input()
    