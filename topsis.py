import numpy as np
import topsis_functions

np.set_printoptions(suppress= True)

data_array = np.loadtxt("matriz_D.csv",delimiter=',',dtype= float)
weights = np.loadtxt("pesos.csv",delimiter=',',dtype= float)
crits = np.genfromtxt("crit.csv",delimiter=',',dtype=str)

num_crit = data_array.shape[1]

normalize_array = topsis_functions.normalize(data_array)
weighted_array = weights * normalize_array

positive_array = topsis_functions.positive_array_calc(weighted_array,num_crit,crits)
negative_array = topsis_functions.negative_array_calc(weighted_array,num_crit,crits)

distance_array_positive = topsis_functions.euclidian_distance(weighted_array,positive_array)
distance_array_negative = topsis_functions.euclidian_distance(weighted_array,negative_array)

proximity_array = topsis_functions.relative_proximity(distance_array_negative,distance_array_positive)

x_names = ["palio","hb20","corolla"]

topsis_functions.plot_bar(x_names,proximity_array)





