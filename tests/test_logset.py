import unittest

import glob
from Nemo.Logset import *

import dataclasses
from dataclasses import dataclass

class TestLogsetBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = LogsetBuilder()
        self.builder.name    = "test log set"
        self.builder.source  = "tests/inputset/source"
        self.builder.destination = "/sphenix/u/jwebb2/stage_test"
        self.builder.files = glob.glob( self.builder.source + '/input*.dat' )
        self.product = self.builder.build()


    def test_has_created_an_logset(self):
        """An logset builder should be able to create an instance of logset"""
        self.assertIsInstance( self.product, Logset )

    def test_has_created_an_logset_with_a_name(self):
        """An log set must provide a name"""
        self.assertIsInstance( self.product.name, str )

    def test_has_created_an_logset_with_a_unique_id(self):
        """An log set shall have a unique identifier"""
        self.assertIsInstance( self.product.unique_id, str )
        
    def test_has_created_an_logset_with_a_source(self):
        """An log set specifies the source of the log files"""
        self.assertIsInstance( self.product.source, str )
        
    def test_has_created_an_logset_with_a_destination(self):
        """An log set specifies the destination of the log files"""
        self.assertIsInstance( self.product.destination, str )
        
    def test_has_created_an_logset_with_a_set_of_files(self):
        """An log set holds a list of all log files"""
        self.assertIsInstance( self.product.files, list )
        
    def test_has_created_an_logset_with_a_status_list(self):
        """An log set will record the status of the log files"""
        self.assertIsInstance( self.product.status, list )
        self.assertEqual( len( self.product.files), len(self.product.status ) )
        
    def test_name_is_immutable(self):
        """The name of the log set is immutable"""
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.name = "changed"

    def test_unique_id_is_immutable(self):
        """The name of the log set is immutable"""
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.unique_id = "changed"
            
    def test_source_is_immutable(self):
        """The source of the log set is immutable"""        
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.source = "changed"
            
    def test_destination_is_immutable(self):
        """The destination of the log set is immutable"""                
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.destination = "changed"

    def test_list_of_files_is_immutable(self):
        """The file list of the log set is immutable"""                
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.files = []

    def test_list_of_status_is_immutable(self):
        """The status_list of the log set is immutable"""                
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.status = []

    def test_elements_in_list_of_files_are_mutable(self):
        """Elements of the list of files are mutable"""
        _saved = self.product.files[0]
        self.product.files[0] = "changed"
        self.assertEqual( self.product.files[0], "changed" )        
        self.product.files[0] = _saved

    def test_elements_in_status_list_are_mutable(self):
        """Elements of the list of files are mutable"""
        _saved = self.product.status[0]
        self.product.status[0] = "changed"
        self.assertEqual( self.product.status[0], "changed" )        
        self.product.status[0] = _saved        
         







if __name__ == '__main__':
        unittest.main()
    

    
       
        





