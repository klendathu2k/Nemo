class Workflow:
    shell      = "bash"
    setup      = "" # global setup policy
    finish     = "" # global finish policy
    def __init__(self):
        self.commands = []

class WorkflowBuilder:

    def __init__(self):
        self.product    = None
        self.commands   = ""
        self.setup      = "#" 
        self.finish     = "#"
        self.shell      = None
        
    def build(self):
        self.product = Workflow()
        self.product.commands.append( "#!/bin/env {}".format(Workflow.shell) )
        self.product.commands.append( Workflow.setup )
        self.product.commands.append( self.setup )
        count = 0
        for line in Workflow.setup.split('\n'):
            count = count + 1
            self.product.commands.append(line)
        for line in self.setup.split('\n'):
            count = count + 1
            self.product.commands.append(line)           
        for line in self.commands.split('\n'):
            count = count + 1
            self.product.commands.append( line )
        for line in self.finish.split('\n'):
            count = count + 1
            self.product.commands.append(line)
        for line in Workflow.finish.split('\n'):
            count = count + 1
            self.product.commands.append(line)            


        print("Returning a new workflow product")
        
        return self.product

                

        
        

    
