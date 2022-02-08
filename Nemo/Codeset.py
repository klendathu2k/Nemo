from dataclasses import dataclass
from prettytable import PrettyTable
import uuid

@dataclass ( frozen = True )
class Codeset:
    name      :   str
    unique_id   : str
    codes       : list[str]
    status      : list[str]
    source      : str
    destination : str

    def __str__(self):

        myname = type(self).__name__
        x = PrettyTable( title="{myname}: {name} {id}".format(myname=myname,name=self.name,id=self.unique_id) )
        x.field_names = ["index","source","destination","file","status"]
        i = 1
        for f, s in zip(self.codes,self.status):        
            x.add_row( [i, self.source, self.destination, f, s] )
            i = i + 1

        return x.get_string()
    
class CodesetBuilder:
    def __init__(self):
        self.name        = ""
        self.product     = None
        self.codes       = []
        self.status      = []
        self.source      = ""
        self.destination = ""

    def build(self):
        self.product=Codeset(
            name        = self.name,
            unique_id   = str(uuid.uuid4()),
            codes       = self.codes,
            source      = self.source,
            destination = self.destination,
            status      = [None] * len(self.codes)
            )
        return self.product

        

        
    
