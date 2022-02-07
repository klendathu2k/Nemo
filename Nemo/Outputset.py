class Outputset:
    def __init__(self):
        pass

class OutputsetBuilder:
    def __init__(self):
        self.product = None

    def build(self):
        self.product = Outputset()
        return self.product

