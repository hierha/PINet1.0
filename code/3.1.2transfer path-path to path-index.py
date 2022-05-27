import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\KEGG\processed\path_map.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\pathway.txt',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'inner',left_on ='path_x', right_on='ID')
data_4 = pd.merge(data_3,data_2,how = 'inner',left_on ='path_y', right_on='ID')
data_5 = data_4[['path_index_x','path_index_y']]
data_5.drop(data_5[data_5.nunique(axis=1) == 1].index, inplace=True)

data_5.to_csv(r'E:\Project\PINet\data_set\relationship\path-path.csv', sep='\t', index =None)

