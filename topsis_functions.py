import numpy as np
import math

def normalize(arr):
    m = arr** 2
    m = np.sqrt(m.sum(axis=0))
    arr = arr / m
    return arr


def euclidian_distance(weighted_array,solutions_array,num_type):
    soma = 0 
    square = 0
    distance_array = np.empty((num_type),dtype=float)
    for i in range(num_type):
        line = weighted_array[i]
        aux_arr = line - solutions_array
        distance_array[i] = math.sqrt(np.sum((aux_arr ** 2)))
        
    return distance_array

def relative_proximity(negative_array,positive_array,num_type):
    proximity_array = np.empty((num_type),dtype= float)
    for i in range (num_type):
        proximity_array[i] = (negative_array[i])/(positive_array[i] + negative_array[i])
    return proximity_array
