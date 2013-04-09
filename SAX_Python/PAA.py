# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:20:30 2013

@author: Jose Javier Valero Mas
@info: Piecewise Aggregate Approximation (PAA) coding 
"""
import numpy;

def PAA_coding_function(data,num_segments):
    # Function to get the PAA coding of data
    # Inputs:
    # -- data : Raw data
    # -- num_segments : Number of segments in which we divide the signal
    #
    # Output:
    # -- PAA_result : Result of applying PAA on data
    
    # PLOTTING ? %
    plotting = 0;
    
    
    # We normalize the signal (mean = 0; standard deviation = 1):
    data_norm = (data-data.mean(axis=0))/data.std(axis=0);
    
    # Length of the data:
    data_length = data.size;
    
    # Number of elements to analyze from the initial data for each segment:
    win_size = numpy.floor(data_length/num_segments);                         
    
    # PAA coding:
    # - In case we do not approximate (number of segments equals length of data):
    if(data_length == num_segments):
        PAA_result = data_norm;
    
    # Convert to PAA:    
    else:
        # data_length is not dividable by num_segments (adding zeros):
        if(data_length/float(num_segments) - win_size):
    
            temp = numpy.empty((num_segments,data_length));
            for i in range(num_segments):
                temp[i,] = data_norm;
            expanded_sub_section = temp.flatten(1);
            
            
            PAA_result = numpy.mean(expanded_sub_section.reshape(num_segments,data_length).transpose(),axis=0);
        # N is divisible by n
        else:                          
            PAA_result = numpy.mean(data_norm.reshape(num_segments,win_size).transpose(),axis=0);
    
    return PAA_result