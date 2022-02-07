from dataclasses import dataclass
import uuid

@dataclass( frozen = True )
class Codeset:
    name        : str
    unique_id   : str
    codes       : list
    status      : list
    source      : str
    destination : str


class CodesetBuilder:
    def __init__(self):
        self.name = ""
        self.unique_id = ""
        self.product = None
        self.codes       = []
        self.status      = []
        self.source      = "."
        self.destination = ""


    def build(self):
        self.product = Codeset(
            name=self.name,
            unique_id=str(uuid.uuid4()),
            source=self.source,
            destination=self.destination,
            codes=self.codes,
            status=[None]*len(self.codes)
            )
        return self.product
