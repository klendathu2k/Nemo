import uuid

class Codeset:
    def __init__(self):
        self.unique_id   = ""
        self.codes       = []
        self.status      = [] # transfer status ...
        self.destination = ""


class CodesetBuilder:
    def __init__(self):
        self.product = None
        self.codes       = []
        self.destination = ""


    def build(self):
        self.product = Codeset()
        self.product.unique_id    = uuid.uuid4()        
        self.product.codes        = self.codes
        if len(self.codes) > 0:
            self.product.status       = [ None ] * len(self.codes)
        self.product.destination  = self.destination
        return self.product
