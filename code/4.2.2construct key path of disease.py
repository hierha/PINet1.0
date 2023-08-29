import numpy as np
from PINet import Key_Path
import csv

for i in range(10):
    flier_path, flier_gene = Key_Path.key_path_gene(i)
    np.save(r'E:\Project\PINet\RWRer\key_path and key_gene\key_path\{}.npy'.format(i), flier_path)
    np.save(r'E:\Project\PINet\RWRer\key_path and key_gene\key_gene\{}.npy'.format(i), flier_gene)

