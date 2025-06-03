import numpy as np
import math

def normalize(arr):
    m = arr** 2
    m = np.sqrt(m.sum(axis=0))
    arr = arr / m
    return arr


def euclidian_distance(weighted_array,solutions_array,num_type):
    
    distance_array = np.empty((num_type),dtype=float)
    
    distance_array = weighted_array - solutions_array
    distance_array = np.power(distance_array,2);
    distance_array = np.sum(distance_array,axis=1)
    distance_array = np.sqrt(distance_array)
        
    return distance_array

def relative_proximity(negative_array,positive_array,num_type):
    proximity_array = np.empty((num_type),dtype= float)
    for i in range (num_type):
        proximity_array[i] = (negative_array[i])/(positive_array[i] + negative_array[i])
    return proximity_array

def positive_array_calc(path,weighted_array,num_crits):
    positive_array = np.empty((num_crits),dtype=float)
    crits = np.genfromtxt(path)
    print(crits)
    for i in range (num_crits):
        collum = weighted_array[:,i]
        if(crits[i] == "c"):
            positive_array[i] = np.min(collum)
        elif(crits[i] == "b"):
            positive_array[i] = np.max(collum)
    return positive_array

def negative_array_calc(path,weighted_array,num_crits):
    negative_array = np.empty((num_crits),dtype=float)
    crits = np.genfromtxt(path,dtype= float)
    for i in range (num_crits):
        collum = weighted_array[:,i]
        if(crits[i] == "c"):
            negative_array[i] = np.max(collum)
        elif(crits[i] == "b"):
            negative_array[i] = np.min(collum)
    return negative_array

            
    
