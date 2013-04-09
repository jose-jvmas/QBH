# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:33:55 2013

@author: Jose Javier Valero Mas
"""

import PAA
import SAX
import numpy

def main():
    #Piecewise Aggregate Aproximation (PAA) coding:
    data = numpy.concatenate((numpy.arange(0,16,1),numpy.arange(16,0,-1)-1),axis=0);
    num_segments = 32;
    alphabet_size = 4;

    PAA_result = PAA.PAA_coding_function(data,num_segments);
    
    SAX_result = SAX.SAX_coding_function(PAA_result,alphabet_size)
    print data
    print PAA_result
    print SAX_result

if __name__ == "__main__":main()