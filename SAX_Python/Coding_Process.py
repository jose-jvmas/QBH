# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:33:55 2013

@author: Jose Javier Valero Mas
@info: Complete coding implentation-> PAA (number of segments) + SAX (number of levels)
"""

import PAA
import SAX

def coding(data,num_segments,alphabet_size):
    # Function to obtain the SAX codification
    # Inputs:
    # -- data : Raw data
    # -- num_segments : Number of segments in which we divide the signal
    # -- alphabet_size : Number of levels for the coding
    #
    # Output:
    # -- SAX_result : Result of applying the complete process on the initial data

    #Piecewise Aggregate Aproximation (PAA) coding:
    PAA_result = PAA.PAA_coding_function(data,num_segments);    
    #Symbolic Aggregate Approximation (SAX) coding:
    SAX_result = SAX.SAX_coding_function(PAA_result,alphabet_size)

    return SAX_result