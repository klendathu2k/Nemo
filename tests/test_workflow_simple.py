import glob
from Nemo.Workflow import *

import dataclasses
from dataclasses import dataclass

builder = WorkflowBuilder()
builder.name = "test workflow"
builder.commands = """
# comment line
root.exe TestMacro.C
"""
builder.setup  = "# comment line"
builder.finish = "# comment line"
product = builder.build()

print(product)
