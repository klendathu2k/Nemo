from dataclasses import dataclass
import uuid

@dataclass ( frozen = True )
class Outputset:
    name      :   str
    unique_id   : str
    files       : list[str]
    status      : list[str]
    source      : str
    destination : str
    
class OutputsetBuilder:
    def __init__(self):
        self.name        = ""
        self.product     = None
        self.files       = []
        self.status      = []
        self.source      = ""
        self.destination = ""

    def build(self):
        self.product=Outputset(
            name        = self.name,
            unique_id   = str(uuid.uuid4()),
            files       = self.files,
            source      = self.source,
            destination = self.destination,
            status      = [None] * len(self.files)
            )
        return self.product

        
    
