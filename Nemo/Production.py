import sys

import datetime
import uuid

class Production:

    facility = "" # eg RHIC
    group    = "" # eg sPHENIX
    

    def __init__(self):

        # Production job identification
        
        self.unique_id          = 0     # a unique identifier for the production job
        self.name               = ""    # a unique human readable name for the production
        self.genre              = ""    # specification of the type of production (MC, real data, ...)
        self.release            = ""    # tag specifying the release of the software used for the production
        self.creation           = None  # creation time for this production
        self.submission         = None  # submission time for this production
        self.resubmission       = []    # how many roads must a man walk down?
        self.identifier         = 0     # identification 

        # Dependencies on other jobs

        self.dependencies       = []    # unique ids of jobs which must be completed prior to this job 

        # File sets required by the production job and (expected to be) returned by the prodction job

        self.code_set           = None  # software, macros, etc... needed to run the production        
        self.input_set          = None  # description of the input data set
        self.output_set         = None  # description of the output data set
        self.log_set            = None  # captured logfiles

        # Job workflow
        self.workflows          = None    # one or more sets of workflows to be executed in this production        
        
class ProductionBuilder:

    def __init__(self):
        self.product           = None
        self.codeset_builder   = None
        self.inputset_builder  = None
        self.outputset_builder = None
        self.logset_builder    = None
        self.workflow_builder  = None

    def SetCodesetBuilder(self,builder):
        self.codeset_builder = builder

    def SetInputsetBuilder(self,builder):
        self.inputset_builder = builder

    def SetOutputsetBuilder(self,builder):
        self.outputset_builder = builder

    def SetLogsetBuilder(self,builder):
        self.logset_builder = builder

    def SetWorkflowBuilder(self,builder):
        self.workflow_builder = builder        

    def build(self,name,genre,release,dependencies=[]):

        self.product              = Production()
        self.product.name         = name  # TODO: enforce uniqueness (check all productions recorded in DB)
        self.product.unique_id    = uuid.uuid4()
        self.product.genre        = genre
        self.product.release      = release
        self.product.dependencies = dependencies
        self.product.creation     = str(datetime.datetime.now())

        if self.codeset_builder != None:
            self.product.code_set = self.codeset_builder.build()

        if self.inputset_builder != None:
            self.product.input_set = self.inputset_builder.build()

        if self.outputset_builder != None:
            self.product.output_set = self.outputset_builder.build()

        if self.logset_builder != None:
            self.product.log_set = self.logset_builder.build()

        if self.workflow_builder != None:
            self.product.workflows = self.workflow_builder.build()

        return self.product

        
        

    

        
        
        

    





