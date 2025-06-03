import numpy as np
import matplotlib.pyplot as plt
import math

def normalize(arr):
    m = arr** 2
    m = np.sqrt(m.sum(axis=0))
    arr = arr / m
    return arr


def euclidian_distance(weighted_array,solutions_array):
    distance_array = weighted_array - solutions_array
    distance_array = np.power(distance_array,2);
    distance_array = np.sum(distance_array,axis=1)
    distance_array = np.sqrt(distance_array)
        
    return distance_array

def relative_proximity(negative_array,positive_array):
    proximity_array= negative_array/(positive_array + negative_array)
    return proximity_array

def positive_array_calc(weighted_array,num_crits,crits):
    positive_array = np.empty((num_crits),dtype=float)
    for i in range (num_crits):
        collum = weighted_array[:,i]
        if(crits[i] == "c"):
            positive_array[i] = np.min(collum)
        elif(crits[i] == "b"):
            positive_array[i] = np.max(collum)
    return positive_array

def negative_array_calc(weighted_array,num_crits,crits):
    negative_array = np.empty((num_crits),dtype=float)
    for i in range (num_crits):
        collum = weighted_array[:,i]
        if(crits[i] == "c"):
            negative_array[i] = np.max(collum)
        elif(crits[i] == "b"):
            negative_array[i] = np.min(collum)
    return negative_array

def plot_bar(x,y):
    fig, ax = plt.subplots(figsize=(40,20))
    ax.bar(x,y,color = "orange")
    plt.show()

                
    
