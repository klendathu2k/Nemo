import unittest

import glob
from Nemo.Codeset import *

import dataclasses
from dataclasses import dataclass

class TestCodesetBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = CodesetBuilder()
        self.builder.name    = "test code set"
        self.builder.source  = "tests/inputset/source"
        self.builder.destination = "/sphenix/u/jwebb2/stage_test"
        self.builder.codes = glob.glob( self.builder.source + '/input*.dat' )
        self.product = self.builder.build()


    def test_has_created_an_inputset(self):
        """An inputset builder should be able to create an instance of inputset"""
        self.assertIsInstance( self.product, Codeset )

    def test_has_created_an_inputset_with_a_name(self):
        """An code set must provide a name"""
        self.assertIsInstance( self.product.name, str )

    def test_has_created_an_inputset_with_a_unique_id(self):
        """An code set shall have a unique identifier"""
        self.assertIsInstance( self.product.unique_id, str )
        
    def test_has_created_an_inputset_with_a_source(self):
        """An code set specifies the source of the input codes"""
        self.assertIsInstance( self.product.source, str )
        
    def test_has_created_an_inputset_with_a_destination(self):
        """An code set specifies the destination of the input codes"""
        self.assertIsInstance( self.product.destination, str )
        
    def test_has_created_an_inputset_with_a_set_of_codes(self):
        """An code set holds a list of all input codes"""
        self.assertIsInstance( self.product.codes, list )
        
    def test_has_created_an_inputset_with_a_status_list(self):
        """An code set will record the status of the input codes"""
        self.assertIsInstance( self.product.status, list )
        self.assertEqual( len( self.product.codes), len(self.product.status ) )
        
    def test_name_is_immutable(self):
        """The name of the code set is immutable"""
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.name = "changed"

    def test_unique_id_is_immutable(self):
        """The name of the code set is immutable"""
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.unique_id = "changed"
            
    def test_source_is_immutable(self):
        """The source of the code set is immutable"""        
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.source = "changed"
            
    def test_destination_is_immutable(self):
        """The destination of the code set is immutable"""                
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.destination = "changed"

    def test_list_of_codes_is_immutable(self):
        """The file list of the code set is immutable"""                
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.codes = []

    def test_list_of_status_is_immutable(self):
        """The status_list of the code set is immutable"""                
        with self.assertRaises( dataclasses.FrozenInstanceError ):
            self.product.status = []

    def test_elements_in_list_of_codes_are_mutable(self):
        """Elements of the list of codes are mutable"""
        _saved = self.product.codes[0]
        self.product.codes[0] = "changed"
        self.assertEqual( self.product.codes[0], "changed" )        
        self.product.codes[0] = _saved

    def test_elements_in_status_list_are_mutable(self):
        """Elements of the list of codes are mutable"""
        _saved = self.product.status[0]
        self.product.status[0] = "changed"
        self.assertEqual( self.product.status[0], "changed" )        
        self.product.status[0] = _saved        
         







if __name__ == '__main__':
        unittest.main()
    

    
       
        





