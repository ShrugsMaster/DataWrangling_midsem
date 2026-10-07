import numpy as np              
a = np.array([[10, 20, 30], [40, 50, 60]])
mean_columns = np.mean(a, axis=0)
print(mean_columns)