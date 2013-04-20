# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:32:51 2013

@author: Jose Javier Valero Mas
@info: Implementation of the Smith-Waterman algorithm for local alignment
"""

import numpy;

def SW():
    x1 = ['a','b','z','z','z','z','d','e'];
    x2 = ['a','b','d','e'];
    
    #We transform the vectors into numpy arrays:
    x1 = numpy.array(x1);
    x2 = numpy.array(x2);
    print type(x1)


    #Dimensions of the vectors:
    length_x1 = x1.shape[0];
    length_x2 = x2.shape[0];
    
    #Values:
    match = 2;
    mismatch = -1;
    delta_insertion = -1;
    delta_deletion = -1;

    #Matrices:
    matrix = numpy.zeros((length_x1+1,length_x2+1),dtype=float); #Forward process
    matrix_back_u = numpy.zeros((length_x1+1,length_x2+1),dtype=float); #Backward process (u axis)
    matrix_back_v = numpy.zeros((length_x1+1,length_x2+1),dtype=float); #Backward process (v axis)
    
    #Array for the the four candidate values at each point in the matrix:
    candidate_values = numpy.zeros((1,4),dtype=float);    
    
    #Filling of the matrices:
    for u in range(1,length_x1+1):
        for v in range(1,length_x2+1):
            #We create the possible candidates for the new value in the
            #matrix:      
            diagonal_value = similarity_score(x1[u-1],x2[v-1],match,mismatch);
            candidate_values[0,0] = matrix[u-1,v-1] + diagonal_value;
            candidate_values[0,1] = matrix[u-1,v] + delta_insertion;
            candidate_values[0,2] = matrix[u,v-1] + delta_deletion;
            candidate_values[0,3] = 0;
                    
            
            #We evaluate those values (find the maximum) and, depending on if
            #is insertion/deletion/match/mismatch/0 we proceed:
            max_value = 0;
            type_index = 0;
            max_value = (candidate_values.max(axis=0)).max(axis=0);
            type_index = (candidate_values.max(axis=0)).argmax(axis=0);
            matrix[u,v] = max_value;
            
            
            #We fill the backwards matrices (one for each index of the
            #matrix):
            if(type_index == 0):
                matrix_back_u[u,v] = u - 1 ;
                matrix_back_v[u,v] = v - 1 ;
            elif(type_index == 1):
                matrix_back_u[u,v] = u - 1 ;
                matrix_back_v[u,v] = v ;
            elif(type_index == 2):
                matrix_back_u[u,v] = u ;
                matrix_back_v[u,v] = v - 1 ;
            elif(type_index == 3):
                matrix_back_u[u,v] = u ;
                matrix_back_v[u,v] = v ;
                
            #For indexing issues, we have to add this value that later will be deducted:
            matrix_back_u[u,v] += 1;
            matrix_back_v[u,v] += 1;    
    
    #We now look for the maxima and their position:
    #aux = numpy.array([[0,3,3],[2,1,0]])
    maximum_val = (matrix.max(axis=1)).max(axis=0); #Maximum value in the matrix
    #occurences = numpy.where(aux == maximum_val)
    array_maxima = (matrix==maximum_val).nonzero(); #Positions of the maxima
    number_of_maxima = array_maxima[0].shape[0]; #Amount of maxima
    
    #Variables for the best alignment (in case there are several maxima):
    best_alignment_number = 0;
    best_score = 0;
    path_u_best = [];
    path_v_best = [];
    
    #We iterate depending on the amount of maxima found:
    for iterations_maxima in range(0,number_of_maxima):    
        reached_init = 1; #Did we reach the initial value?
        score = 0; #Score of the alignment
    
        current_u = array_maxima[0][iterations_maxima]; #Current value of u is where the maximum is
        current_v = array_maxima[1][iterations_maxima] #Current value of v is where the maximum is
        next_u = matrix_back_u[current_u,current_v]; #Next u value is pointed out by matrix_back_u
        next_v = matrix_back_v[current_u,current_v]; #Next v value is pointed out by matrix_back_v
        
        path_u = [];
        path_v= [];
        
        while(reached_init > 0):
            if(next_u-1 != current_u):
                path_u.append(x1[current_u-1]);
            else:
                path_u.append('-')
            
            if(next_v-1 != current_v):
                path_v.append(x2[current_v-1]);
            else:
                path_v.append('-')           
            
            
            
            
            #We update the score of the alignment:
            score += matrix[current_u,current_v];
 
            #For next iteration:
            current_u = next_u-1;
            current_v = next_v-1;
            next_u = matrix_back_u[current_u,current_v];
            next_v = matrix_back_v[current_u,current_v];  
            
            #In case current and next positions coincide or either next_u or
            #next_v are 0, we have to finish the loop:
            if (((current_u == next_u-1) and (current_v == next_v-1)) or (next_u == 0) or (next_v == 0)):
                reached_init = 0;

        #Results of the alignment:
        print "Possible Alignment #" + str(iterations_maxima+1) + ":";
        print "Score of the alignment: " + str(score);
        print path_u[::-1];
        print path_v[::-1];
        
        #We only store the best alignment of all the possible ones pointed out by the maxima:
        if(score > best_score):
            best_score = score;
            best_alignment_number = iterations_maxima;
            path_u_best = path_u[::-1];
            path_v_best = path_v[::-1];
    
    #We output the best alignment:
    print "------ BEST ALIGNMENT ------";
    print "Alignment #" + str(best_alignment_number) + " - Score: " + str(best_score);
    print path_u_best
    print path_v_best
    

    
#Function for calculating the similarity between two strings
def similarity_score(val1,val2,match,mismatch):
    if(val1==val2):
        output_value_similarity = match;
    else:
        output_value_similarity = mismatch;
    return output_value_similarity;
