import glob
from Nemo.Inputset import *

builder = InputsetBuilder()
builder.name    = "test input set"
builder.source  = "tests/inputset/source"
builder.destination = "/sphenix/u/jwebb2/stage_test"
builder.files = glob.glob( builder.source + '/input*.dat' )

product = builder.build()

print(str(product))
