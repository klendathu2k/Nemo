from dataclasses import dataclass
import uuid

@dataclass( frozen = True )
class Workflow:
    name      : str
    unique_id : str
    shell     : str 
    commands  : list

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
        #--------------------------------------------------------------------        
        """
        command_setup  = self.setup
        command_user   = self.commands
        command_finish = self.finish
        command_block = '\n'.join([command_shell,command_header,command_setup,command_user,command_finish])

        commands = command_block.split()

        self.product = Workflow(
            name       = self.name,
            unique_id  = str(uuid.uuid4()),
            shell      = self.shell,
            commands   = commands )
        
        return self.product

                

        
        

    
