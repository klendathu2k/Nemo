import glob
from Nemo.Codeset import *

builder = CodesetBuilder()
builder.name    = "test input set"
builder.source  = "tests/inputset/source"
builder.destination = "/sphenix/u/jwebb2/stage_test"
builder.codes = glob.glob( builder.source + '/input*.dat' )

product = builder.build()

print(str(product))
