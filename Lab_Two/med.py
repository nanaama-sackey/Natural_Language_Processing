#!/usr/bin/env python
# coding: utf-8

# # Nana Ama Atombo-Sackey##
#     Lab Two
#     1st October, 2018
#     Calculating Minimum edit distance between two words

# In[18]:


import sys 

def min_edit_distance( source, target ):
   subs_cost = 2
   insert_cost = 1 
   delete_cost = 1
   source_length = len( source )
   target_length = len( target )

   matrix = [ [0] * (target_length + 1) for i in range(source_length + 1) ] #the matrix whose last element -> edit distance

   for i in range( 0, source_length + 1 ): #initialization of base case values
      matrix[i][0] = i
   for j in range( 0, target_length + 1 ):
      matrix[0][j] = j
   for i in range ( 1, source_length + 1 ):
      for j in range( 1, target_length + 1 ):
         if source[i - 1] == target[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1]
         else:
            matrix[i][j] = min(
               matrix[i][j - 1] + insert_cost,
               matrix[i - 1][j] + delete_cost,
               matrix[i - 1][j - 1] + subs_cost
            )
   print("The minimum edit distance between" ,source, "and", target, "is: " ,matrix[i][j] )

#This is to make it possible to run the py file from the cmd	
min_edit_distance( str(sys.argv[1]), str(sys.argv[2]) );
#min_edit_distance("intention","execution")

