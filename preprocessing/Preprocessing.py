from utils import CheckDP


class Preprocessor:
    
    def __init__(self):
        self.cdp = CheckDP()

    def dp(self, data):
        data = self.cdp.checkdp(data)
        return data
