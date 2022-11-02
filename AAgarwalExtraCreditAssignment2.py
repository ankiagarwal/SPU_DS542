# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:25:04 2022

@author: ankia
"""

import math

def largest_PF(number):  
    factor = 2  
    while factor * factor <= number:  # there can be only one factor greater 
                                      # than the sqrt of number
        if number % factor:           # checking if there is a remainder,
                                      # if yes, then skipping to next integer
            factor += 1  
        else:  
            number = number // factor  # if remainder is 0, that means we found 
                                       # a factor, the resultant (number/i) 
                                       # would be another factor and greater   
                                       # than the initial factor i.
    return number  
  
largest_PF(600851475143) 