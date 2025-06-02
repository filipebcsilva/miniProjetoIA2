import numpy as np
import math
import matplotlib.pyplot as plt
import topsis_functions

np.set_printoptions(suppress= True)

data_array = np.loadtxt("matriz_D.csv",delimiter=',',dtype= float)
weights = np.loadtxt("pesos.csv",delimiter=',',dtype= float)

num_type = data_array.shape[0]
num_crit = data_array.shape[1]

normalize_array = topsis_functions.normalize(data_array)
weighted_array = weights * normalize_array

gas_consume = weighted_array[:,0]
confort = weighted_array[:,1]
price = weighted_array[:,2]
rating = weighted_array[:,3]

positive_array = np.array([np.min(gas_consume),np.max(confort),np.min(price),np.max(rating)])
negative_array = np.array([np.max(gas_consume),np.min(confort),np.max(price),np.min(rating)])

distance_array_positive = topsis_functions.euclidian_distance(weighted_array,positive_array,num_type)
distance_array_negative = topsis_functions.euclidian_distance(weighted_array,negative_array,num_type)

proximity_array = topsis_functions.relative_proximity(distance_array_negative,distance_array_positive,num_type)

car_names = ["palio","hb20","corolla"]

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(car_names,proximity_array,color = "blue")
plt.xticks(car_names)
plt.show()






