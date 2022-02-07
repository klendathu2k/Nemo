import unittest

import glob
from Nemo.Production import *
from Nemo.Codeset import *
from Nemo.Inputset import *
from Nemo.Outputset import *
from Nemo.Logset import *
from Nemo.Workflow import *

import dataclasses
from dataclasses import dataclass

from beeprint import pp as pprint    # pip install beeprint

class TestProductionBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = ProductionBuilder()
        self.builder.name  = "test production"
        self.builder.genre = "MC.test"
        self.builder.release = "Library01"
        self.builder.dependencies = ["depend1","depend2"]

        # Codeset builder
        self.csbuilder = CodesetBuilder()
        self.csbuilder.name    = "test code set"
        self.csbuilder.source  = "tests/inputset/source"
        self.csbuilder.destination = "/sphenix/u/jwebb2/stage_test"
        self.csbuilder.codes = glob.glob( self.csbuilder.source + '/input*.dat' )
        self.builder.SetCodesetBuilder( self.csbuilder )

        # Inputset builder
        self.isbuilder = InputsetBuilder()
        self.isbuilder.name    = "test input set"
        self.isbuilder.source  = "tests/inputset/source"
        self.isbuilder.destination = "/sphenix/u/jwebb2/stage_test"
        self.isbuilder.files = glob.glob( self.isbuilder.source + '/input*.dat' )
        self.builder.SetInputsetBuilder( self.isbuilder )

        # Outputset builder
        self.osbuilder = OutputsetBuilder()
        self.builder.SetOutputsetBuilder( self.osbuilder )

        # Logset builder
        self.lsbuilder = LogsetBuilder()
        self.builder.SetLogsetBuilder( self.lsbuilder )                

        # Workflow builder
        self.wfbuilder = WorkflowBuilder()
        self.wfbuilder.name = "test workflow"
        self.wfbuilder.commands = """
        # comment line
        root.exe TestMacro.C
        """
        self.wfbuilder.setup  = "# comment line"
        self.wfbuilder.finish = "# comment line"
        self.builder.SetWorkflowBuilder( self.wfbuilder )

        self.product = self.builder.build()

    def test_build_production(self):
        """Production builder should be able to build a production"""

        self.assertIsInstance( self.product, Production )

    def test_production_has_a_name(self):
        """Each production should have a name"""
        self.assertIsInstance(self.product.name, str )
        self.assertNotEqual( self.product.name, "" )

    def test_production_has_a_unique_id(self):
        """Each production has a unique id"""
        self.assertIsInstance( self.product.unique_id, str )
        self.assertNotEqual( self.product.name, "" )

    def test_production_has_a_genre(self):
        self.assertIsInstance( self.product.genre, str )
        self.assertNotEqual( self.product.genre, "" )

    def test_production_has_a_release(self):
        self.assertIsInstance( self.product.release, str )
        self.assertNotEqual( self.product.release, "" )

    def test_production_has_a_creation(self):
        self.assertIsInstance( self.product.creation, str )
        self.assertNotEqual( self.product.creation, "" )

    def test_production_has_a_list_of_submissions(self):
        self.assertIsInstance( self.product.submission, list )

    def test_production_list_of_submissions_is_initially_empty(self):        
        self.assertEqual( self.product.submission, [] )                

    def test_production_has_a_list_of_job_ids(self):
        self.assertIsInstance( self.product.job_id, list )

    def test_production_list_of_job_ids_is_initially_empty(self):        
        self.assertEqual( self.product.job_id, [] )

    def test_production_has_a_list_of_dependencies(self):
        self.assertIsInstance( self.product.dependencies, list )

    def test_production_has_a_list_of_codeset(self):
        self.assertIsInstance( self.product.codeset, list )

    def test_production_has_a_list_of_inputset(self):
        self.assertIsInstance( self.product.inputset, list )

    def test_production_has_a_list_of_outputset(self):
        self.assertIsInstance( self.product.outputset, list )
        
    def test_production_has_a_list_of_logset(self):
        self.assertIsInstance( self.product.logset, list )

        

        
        


