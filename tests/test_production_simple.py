import glob
from Nemo.Production import *
from Nemo.Codeset import *
from Nemo.Inputset import *
from Nemo.Outputset import *
from Nemo.Logset import *
from Nemo.Workflow import *

import dataclasses
from dataclasses import dataclass

builder = ProductionBuilder()
builder.name  = "test production"
builder.genre = "MC.test"
builder.release = "Library01"
builder.dependencies = ["depend1","depend2"]

        # Codeset builder
csbuilder = CodesetBuilder()
csbuilder.name    = "test code set"
csbuilder.source  = "tests/inputset/source"
csbuilder.destination = "/sphenix/u/jwebb2/stage_test"
csbuilder.codes = glob.glob( csbuilder.source + '/input*.dat' )
builder.SetCodesetBuilder( csbuilder )

        # Inputset builder
isbuilder = InputsetBuilder()
isbuilder.name    = "test input set"
isbuilder.source  = "tests/inputset/source"
isbuilder.destination = "/sphenix/u/jwebb2/stage_test"
isbuilder.files = glob.glob( isbuilder.source + '/input*.dat' )
builder.SetInputsetBuilder( isbuilder )

        # Outputset builder
osbuilder = OutputsetBuilder()
osbuilder.name    = "test output set"
osbuilder.source  = "tests/inputset/source"
osbuilder.destination = "/sphenix/u/jwebb2/stage_test"
osbuilder.files = glob.glob( isbuilder.source + '/input*.dat' )
builder.SetOutputsetBuilder( osbuilder )

        # Logset builder
lsbuilder = LogsetBuilder()
lsbuilder.name    = "test log set"
lsbuilder.source  = "tests/inputset/source"
lsbuilder.destination = "/sphenix/u/jwebb2/stage_test"
lsbuilder.files = glob.glob( isbuilder.source + '/input*.dat' )
builder.SetLogsetBuilder( lsbuilder )                

        # Workflow builder
wfbuilder = WorkflowBuilder()
wfbuilder.name = "test workflow"
wfbuilder.commands = """
        # comment line
        root.exe TestMacro.C
        """
wfbuilder.setup  = "# comment line"
wfbuilder.finish = "# comment line"
builder.SetWorkflowBuilder( wfbuilder )

product = builder.build()

print("Print as string")
print(str(product))

print("Render as HTML")
print( product.render("html") )
print ("Render as JSON")
print( product.render("json") )
print( "Render as csv" )
print( product.render("csv") )
print( "Render as YAML" )
print( product.render("yaml") )

