# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:20:30 2013

@author: Jose Javier Valero Mas
@info: Piecewise Aggregate Approximation (PAA) coding 
"""
import numpy;
import csv;

def SAX_coding_function(PAA_in,alphabet_size):
    #Function to get the PAA coding of data
    #inputs:
    #-- PAA_in : Input data processed represented as PAA
    #-- alphabet_size : Number of levels for the coding
    #
    #Output:
    #-- SAX_result : Result of applying SAX on data

    #We obtain the SAX cut points by looking to a certain distribution:
    cut_points = read_levels_distribution(alphabet_size);
   
    #We initialize the outputs of SAX: levels and codes
    SAX_result_level = numpy.empty((PAA_in.size));
    SAX_result = numpy.chararray(PAA_in.size);
    
    #Equivalence leve-string for SAX:
    string_equivalent = numpy.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']);
    
    #We go through the PAA data and we code it according to SAX:
    for i in range(PAA_in.size):
        #We check where, in the borders of the distribution, our sample is:
        SAX_result_level[i] = numpy.count_nonzero(cut_points <= PAA_in[i]);
        #We code the level:
        SAX_result[i] = string_equivalent[SAX_result_level[int(i)]-1];
    write_SAX_result(SAX_result);
    return SAX_result


#Function to write the result in a CSV file:
def write_SAX_result(SAX_result):
    with open('./Results/SAX_Approximation.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(SAX_result)

    #PARA DESPUES PODER LEER -> numpy.array(line) (CASTING)

    
#Function to read the cut points of a distribution:
def read_levels_distribution(alphabet_size):
    #Function to read the cut points for SAX:
    #inputs:
    #-- alphabet_size : Number of levels for the coding
    #
    #Output:
    #-- cut_points : Cut points depending on the distribution
    
    #We read the file of the distribution:
    file_read = csv.reader(open("./Distributions/Normal_Distribution.csv"));
    
    #We find the suitable level:
    if(alphabet_size > 2):
        for i in range(0,alphabet_size-1):
            line = file_read.next();
    else:
        line = file_read.next();
    
    #We cast the read line into a numpy array of floats:
    cut_points = numpy.array(line,dtype=float);
    
    return cut_points
    