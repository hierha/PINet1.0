import numpy as np
import pandas as pd
from PINet import association_matrix

normal_state_num = 1
path_num = 345
association_matrix.association_matrix(normal_state_num, path_num, r'E:\Project\PINet\RWRer\normal state\normal state-path.csv', r'E:\Project\PINet\RWRer\normal state\matrix\normal_state-path.npy')

