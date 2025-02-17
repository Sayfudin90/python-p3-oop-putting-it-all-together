#!/usr/bin/env python3

from shoe import Shoe

import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        stan_smith = Shoe("Adidas", 9)
        assert(stan_smith.brand == "Adidas")
        assert(stan_smith.size == 9)

    def test_requires_int_size(self):
     '''prints "size must be an integer" if size is not an integer.'''
    captured_out = io.StringIO()  # Create a StringIO object to capture printed output
    sys.stdout = captured_out  # Redirect stdout to the StringIO object
    stan_smith = Shoe("Adidas", "not an integer")  # This should trigger the print statement
    sys.stdout = sys.__stdout__  # Reset stdout to its original value
    assert captured_out.getvalue() == "size must be an integer\n"  # Check if the correct message was printed

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Your shoe is as good as new!\n")
    
    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9)
        stan_smith.cobble()
        assert(stan_smith.condition == "New")
        
        
   
