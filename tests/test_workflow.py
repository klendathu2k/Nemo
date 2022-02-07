import unittest

import glob
from Nemo.Workflow import *

import dataclasses
from dataclasses import dataclass

from beeprint import pp as pprint    # pip install beeprint

class TestWorkflowBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = WorkflowBuilder()
        self.builder.name = "test workflow"
        self.builder.commands = """
        # comment line
        root.exe TestMacro.C
        """
        self.builder.setup  = "# comment line"
        self.builder.finish = "# comment line"
        self.product = self.builder.build()

    def test_has_created_a_workflow(self):
        """A workflow builder should create an instance of Workflow"""
        self.assertIsInstance(self.product, Workflow)

    def test_has_created_an_inputset_with_a_name(self):
        """An input set must provide a name"""
        self.assertIsInstance( self.product.name, str )

    def test_has_created_an_inputset_with_a_unique_id(self):
        """An input set shall have a unique identifier"""
        self.assertIsInstance( self.product.unique_id, str )


    def test_has_created_an_inputset_with_a_shell(self):
        """An input set must provide a shell"""
        self.assertIsInstance( self.product.shell, str )
        self.assertEqual( self.product.shell, self.builder.shell )

    def test_has_created_an_inputset_with_default_shell_as_bash(self):
        """An input set must provide a shell"""
        self.assertIsInstance( self.product.shell, str )
        self.assertEqual( self.product.shell, "bash" )

    def test_has_created_an_inputset_with_list_of_commands(self):
        """An input set must provide a list of commands"""
        self.assertIsInstance( self.product.commands, list )

    def test_has_created_an_inputset_with_list_of_commands(self):
        """An input set must provide a shell"""
        self.assertIsInstance( self.product.commands, list )        

    def test_name_is_immutable(self):
        """The name of the workflow is immutable"""        
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.name = "changed"        

    def test_unique_id_is_immutable(self):
        """The unique_id of the workflow is immutable"""        
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.unique_id = "changed"

    def test_shell_is_immutable(self):
        """The shell of the workflow is immutable"""        
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.shell = "changed"
            
    def test_list_of_commands_is_immutable(self):
        """The name of the workflow is immutable"""        
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.commands = []

            
