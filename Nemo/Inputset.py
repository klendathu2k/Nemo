from dataclasses import dataclass

import uuid

@dataclass ( frozen = True )
class Inputset:
    name      :   str
    unique_id   : str
    files       : list[str]
    status      : list[str]
    source      : str
    destination : str
    
    

#class Inputset:
#    def __init__(self):
#        self.local_inputs  = []
#        self.remote_inputs = []
#        self.transfer

class InputsetBuilder:
    def __init__(self):
        self.name        = ""
        self.product     = None
        self.files       = []
        self.status      = []
        self.source      = ""
        self.destination = ""

    def build(self):
        self.product=Inputset(
            name        = self.name,
            unique_id   = str(uuid.uuid4()),
            files       = self.files,
            source      = self.source,
            destination = self.destination,
            status      = [None] * len(self.files)
            )
        return self.product

        
    
