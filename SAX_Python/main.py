# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:33:55 2013

@author: Jose Javier Valero Mas
@info: Example using the coding with a main function. Data is artificial
"""

import PAA
import SAX
import numpy
import matplotlib.pyplot as plt

def main():
    data = numpy.concatenate((numpy.arange(0,16,1),numpy.arange(16,0,-1)-1),axis=0);
    num_segments = 8;
    alphabet_size = 2;

    #Piecewise Aggregate Aproximation (PAA) coding:
    PAA_result = PAA.PAA_coding_function(data,num_segments);
    
    #Symbolic Aggregate Approximation (SAX) coding:
    SAX_result = SAX.SAX_coding_function(PAA_result,alphabet_size)
    
    """
    print data
    plt.plot(data,label='Data')

    plt.plot(PAA_result,'r',label='PAA')
    plt.legend(bbox_to_anchor=(0.85, 1), loc=2, borderaxespad=0.)
    plt.show()



    print PAA_result
    """
    print SAX_result
    

if __name__ == "__main__":main()
