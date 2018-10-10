#!/usr/bin/env python
# coding: utf-8

#  ### Natural Language Processing ###
#   # A Naive Bayes Classifier 
#   #  Name: Nana Ama Atombo-Sackey
#   #    Lab One

# In[3]:


import sys
import re
import random
from math import *
#reading files to train on.
def readFile(files):
    data = {
        0:[],
        1:[]}
    for file in files:
        for line in open(file):
            # getting rid of all regular expressions not needed
            review = line.split('\n')
            review = review[0].split('\t')
            features = re.sub(r"[&)#-=$!(%)]+","",review[0])   
            label = int(review[1])
            if label == 0:
                data[0].append(features.split())
            else:
                data[1].append(features.split())
            
    print("The total words in the negative class is: " , len(data[0])) 
    print("The total words in the positive class is: " , len(data[1])) 
    return data
corpus= readFile(['amazon_cells_labelled.txt',"imdb_labelled.txt","yelp_labelled.txt"])
    


#  #### Calculating log prior and loglikelihood by implementing it in the trian function below ##

# In[4]:


def train(doc):
    #Initializng the logprior and Loglikehood
    classes= [0,1]
    prior = dict()
    likelihood= {
        0:{},
        1:{}
    }
    numOfDocD = len(doc[0])+len(doc[1])
    wordCount = {
        0:{},
        1:{}
    }
    print("The number of documents in D(corpus) is :", numOfDocD)
    
    #calculating log prior
    for c in classes:
        numOfDocClass = len(doc[c])
        prior[c] = log((numOfDocClass/numOfDocD))
              
    print("The number of documents from Corpus in the class is: ",numOfDocClass)
    print("The logpriority is: ", prior)
    
    
   # Calculating log likelihood
    for c in doc:
        for reviews in doc[c]:

            for words in reviews:
                if words in wordCount[c]:
                    wordCount[c][words]+=1
                else:
                    wordCount[c][words]=1
    
    vocabulary = []
    for c in classes:
        vocabulary += list(wordCount[c].keys()) 
    vocabulary = set(vocabulary)
    for words in vocabulary:
        for c in classes:
            if words in wordCount[c]:
                likelihood[c][words] = log( ((wordCount[c][words] + 1)/(sum(wordCount[c].values())+len(vocabulary))) )
            else:
                 likelihood[c][words] = log(((1)/(sum(wordCount[c].values())+len(vocabulary))) )
 
    return prior,likelihood,vocabulary
prior,likelihood,vocabulary=train(corpus)


# #### Implementing Test Function and Results File or Output ####

# In[5]:


def test(doc, prior, likelihood,vocabulary):
    summ = dict()
    for c in [0,1]:
        summ[c]= prior[c]
        for word in doc.split():
            if word in vocabulary:
                summ[c] = summ[c] + likelihood[c][word]
    print(summ)
    if summ[0]> summ[1]:
        return 0 
    else:
        return 1
    return vocabulary


def read(file):
    read_me = open(file, "r") #Reading file
    write_file = open("results_file.txt", "w") # Writing to file
    finalRead = read_me.readline()
    while (len(finalRead)!= 0):
        finalRead = re.sub(r"[&)#-=$!(%)<>]+.@","",finalRead.lower())
        result = test(finalRead, prior,likelihood,vocabulary)
        print(finalRead,result)
        write_file.write(str(result) + str("\n"))
        finalRead = read_me.readline()


# In[ ]:


if __name__ == "__main__":
    read(sys.argv[1])
else:
    print("Unable to take file please")

