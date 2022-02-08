import glob
from Nemo.Logset import *

builder = LogsetBuilder()
builder.name    = "test log set"
builder.source  = "tests/inputset/source"
builder.destination = "/sphenix/u/jwebb2/stage_test"
builder.files = glob.glob( builder.source + '/input*.dat' )

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
