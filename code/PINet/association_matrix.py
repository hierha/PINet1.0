import numpy as np
import pandas as pd

def association_matrix(x, y, association_file, out_file):
    association_martix = np.zeros((x,y))
    df_1 = pd.read_csv(association_file, sep='\t', dtype=np.int64)
    if x > 1:
        for row in df_1.itertuples(index=False, name=None):
            index_x, index_y = row
            association_martix[index_x][index_y] = 1
        np.save(out_file,association_martix)
    else:
        for row in df_1.itertuples(index=False, name=None):
            index_y = row[0]
            association_martix[0,index_y] = 1
        np.save(out_file,association_martix)
