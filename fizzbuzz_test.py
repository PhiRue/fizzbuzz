#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:00:23 2019

@author: philineruehl
"""

from fizzbuzz import fizzbuzz

def test_passing_3_returns_fizz():
    assert fizzbuzz(3) == 'FIZZ'
    assert fizzbuzz(99) == 'FIZZ'    
    assert fizzbuzz(15) == 'FIZZ'
    
def test_passinf_5_returns_buzz():
    assert fizzbuzz(5) == 'BUZZ'
    assert fizzbuzz(10) == 'BUZZ'
    assert fizzbuzz(20) == 'BUZZ'
    
def test_passing_other_number_reutnrs_itself():
    assert fizzbuzz(4) == 4    
    assert fizzbuzz(1) == 1