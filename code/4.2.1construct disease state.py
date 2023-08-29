from PINet import RWR
import numpy as np

for disease_index in range(10):
    disease_state = RWR.RWRer([disease_index], r'E:\Project\PINet\RWRer\matrix\disease-path.npy', r'E:\Project\PINet\RWRer\matrix\disease-gene.npy', r'E:\Project\PINet\RWRer\matrix\path-gene.npy', r'E:\Project\PINet\RWRer\matrix\path-path.npy', r'E:\Project\PINet\RWRer\matrix\gene-gene.npy', 0.5)
    np.save(r'E:\Project\PINet\RWRer\disease state\{}.npy'.format(disease_index), disease_state)
