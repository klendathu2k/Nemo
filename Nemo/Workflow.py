from dataclasses import dataclass
import uuid
from prettytable import PrettyTable

@dataclass( frozen = True )
class Workflow:
    name      : str
    unique_id : str
    shell     : str 
    commands  : list

    def __str__(self):
        myname = type(self).__name__
        width = 0
        for command in self.commands:
            if len(command) > width:
                width = len(command)
        x = PrettyTable(
            title="{myname}: {name} {id}".format(myname=myname,name=self.name,id=self.unique_id),
            min_table_width = width + 10
            )
        
        x.field_names = ["index", "command"]
        x.align["command"]="l"
        i = 1
        for command in self.commands:            
            x.add_row([i, command])
            i = i + 1

        return x.get_string()

class WorkflowBuilder:

    def __init__(self):
        self.product    = None
        self.commands   = ""
        self.setup      = "#" 
        self.finish     = "#"
        self.shell      = "bash" # Default command shell
        
    def build(self):

        # Build the command script
        command_shell =  "!/bin/env " + self.shell
        command_header = """
#--------------------------------------------------------------------
# Nemo default workflow builder
#--------------------------------------------------------------------"""
        command_setup  = self.setup
        command_user   = self.commands
        command_finish = self.finish
        command_block = '\n'.join([command_shell,command_header,command_setup,command_user,command_finish])

        commands = command_block.split('\n')

        self.product = Workflow(
            name       = self.name,
            unique_id  = str(uuid.uuid4()),
            shell      = self.shell,
            commands   = commands )
        
        return self.product

                

        
        

    
