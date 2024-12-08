import numpy as np

data = np.array([72,75,80,85,90,85,80,75,72,70,72])

def delay_embedding(data, delay, dim):
    n = len(data)
    return np.array(data[i:n-(dim-1)*delay+i:delay] for i in range(dim)]).T

embedded_data = 