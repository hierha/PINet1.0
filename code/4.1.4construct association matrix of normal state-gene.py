import numpy as np
import pandas as pd
from PINet import association_matrix

normal_state_num = 1
gene_num = 18532
association_matrix.association_matrix(normal_state_num, gene_num, r'E:\Project\PINet\RWRer\normal state\normal state-gene.csv', r'E:\Project\PINet\RWRer\normal state\matrix\normal_state-gene.npy')