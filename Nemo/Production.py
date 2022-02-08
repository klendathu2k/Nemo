import sys
import datetime
import uuid
from dataclasses import dataclass
from prettytable import PrettyTable

@dataclass( frozen = True )
class Production:

    # Production job identification
    name               : str     # a unique human readable name for the production        
    unique_id          : str     # a unique identifier for the production job
    genre              : str     # specification of the type of production (MC, real data, ...)
    release            : str     # tag specifying the release of the software used for the production
    creation           : str     # creation time for this production
    submission         : list    # submission time(s) for this production
    job_id             : list    # job identifier(s)

    # Dependencies on other jobs

    dependencies   : list    # unique ids of jobs which must be completed prior to this job 

    # File sets required by the production job and (expected to be) returned by the prodction job

    codeset           : list  # software, macros, etc... needed to run the production        
    inputset          : list  # description of the input data set
    outputset         : list  # description of the output data set
    logset            : list  # captured logfiles

    # Job workflow
    workflows          : list    # one or more sets of workflows to be executed in this production

    facility : str = "RHIC" 
    group    : str = "sPHENIX"

    def __str__(self):
        return self.render(method = "string")

    def render(self, method ):    
        myname = type(self).__name__
 
        x = PrettyTable(
            title="{myname}: {name} {id}".format(myname=myname,name=self.name,id=self.unique_id)
            )
 
        x.field_names = ["facility", "group", "proudction type","software release","creation date" ]
        x.add_row( [self.facility, self.group, self.genre, self.release, self.creation ] )

        result = "ERROR: method not recognized"

        if method == "string":
            result = result + x.get_string() + "\n\n"
            for code in self.codeset:
                result = result + str(code) + "\n\n"
            for inset in self.inputset:
                result = result + str(inset) + "\n\n"
            for outset in self.outputset:
                result = result + str(outset) + "\n\n" 
            for logset in self.logset:
                result = result + str(logset) + "\n\n"
            for work in self.workflows:
                result = result + str(work) + "\n\n"

        if method == "html":
            result = result + x.get_html_string() + "\n\n"
            for code in self.codeset:
                result = result + code.render("html") + "\n\n"
            for inset in self.inputset:
                result = result + inset.render("html") + "\n\n"
            for outset in self.outputset:
                result = result + outset.render("html") + "\n\n" 
            for logset in self.logset:
                result = result + logset.render("html") + "\n\n"
            for work in self.workflows:
                result = result + work.render("html") + "\n\n"

        if method == "csv":
            result = result + x.get_csv_string() + "\n\n"
            for code in self.codeset:
                result = result + code.render("csv") + "\n\n"
            for inset in self.inputset:
                result = result + inset.render("csv") + "\n\n"
            for outset in self.outputset:
                result = result + outset.render("csv") + "\n\n" 
            for logset in self.logset:
                result = result + logset.render("csv") + "\n\n"
            for work in self.workflows:
                result = result + work.render("csv") + "\n\n"

        if method == "json":
            result = result + x.get_json_string() + "\n\n"
            for code in self.codeset:
                result = result + code.render("json") + "\n\n"
            for inset in self.inputset:
                result = result + inset.render("json") + "\n\n"
            for outset in self.outputset:
                result = result + outset.render("json") + "\n\n" 
            for logset in self.logset:
                result = result + logset.render("json") + "\n\n"
            for work in self.workflows:
                result = result + work.render("json") + "\n\n"

        if method == "latex":
            result = result + x.get_latex_string() + "\n\n"
            for code in self.codeset:
                result = result + code.render("latex") + "\n\n"
            for inset in self.inputset:
                result = result + inset.render("latex") + "\n\n"
            for outset in self.outputset:
                result = result + outset.render("latex") + "\n\n" 
            for logset in self.logset:
                result = result + logset.render("latex") + "\n\n"
            for work in self.workflows:
                result = result + work.render("latex") + "\n\n"                                 

        return result
 

        
       
        
class ProductionBuilder:

    def __init__(self):

        self.name = ""
        self.genre = ""
        self.release = ""
        self.submission = []
        self.job_id = []
        self.depenencies = []
        
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

    def build(self):

        self.product = Production(
            name         = self.name,
            unique_id    = str(uuid.uuid4()),
            genre        = self.genre,
            release      = self.release,
            creation     = str(datetime.datetime.now()),
            submission   = self.submission,
            job_id       = self.job_id,
            dependencies = self.dependencies,
            codeset      = [ self.codeset_builder.build()],
            inputset     = [ self.inputset_builder.build()],
            outputset    = [ self.outputset_builder.build()],
            logset       = [ self.logset_builder.build()],
            workflows    = [ self.workflow_builder.build()]
            )

#       self.product              = Production()
#       self.product.name         = name  # TODO: enforce uniqueness (check all productions recorded in DB)
#       self.product.unique_id    = uuid.uuid4()
#       self.product.genre        = genre
#       self.product.release      = release
#       self.product.dependencies = dependencies
#       self.product.creation     = str(datetime.datetime.now())
#
#       if self.codeset_builder != None:
#           self.product.code_set = self.codeset_builder.build()
#       if self.inputset_builder != None:
#           self.product.input_set = self.inputset_builder.build()
#       if self.outputset_builder != None:
#           self.product.output_set = self.outputset_builder.build()
#       if self.logset_builder != None:
#           self.product.log_set = self.logset_builder.build()
#       if self.workflow_builder != None:
#           self.product.workflows = self.workflow_builder.build()

        return self.product

        
        

    

        
        
        

    





