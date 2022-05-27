import numpy as np
import pandas as pd
from PINet import association_matrix

path_num = 345
drug_num = 6259
association_matrix.association_matrix(drug_num, path_num, r'E:\Project\PINet\data_set\relationship\processed\drug-path.csv', r'E:\Project\PINet\RWRer\matrix\drug-path.npy')
print('drug-path is finished')

