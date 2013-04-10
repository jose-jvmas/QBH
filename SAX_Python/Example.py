# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:54:10 2013

@author: Jose Javier Valero Mas
@info: Basic example of SAX coding using a melody extracted with MELODIA
"""

import csv
import numpy
import Coding_Process;
import matplotlib.pyplot as plt

## We get the corresponding csv file:
file_read = csv.reader(open('q6.csv'));
## We check the length of the csv file:
size_of_csv = len(list(csv.reader(open('q6.csv')))) 

## We take all the content of the file (pitch content) to a variable:
index = 0;
a = numpy.zeros(size_of_csv)
for time,freq in file_read:
    if(float(freq) < 0):
        a[index] = 0;
    else:
        #if(float(freq)<440):
        #    a[index] = round(12*math.log(float(freq)/440,2))%-12;
        #else:
        #    a[index] = round(12*math.log(float(freq)/440,2))%12;
        a[index] = freq;
    index = index + 1;


SAX_result = Coding_Process.coding(a,1024,12);
print SAX_result
