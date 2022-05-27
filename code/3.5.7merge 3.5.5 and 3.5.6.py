import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\relationship\disease-gene from CTD.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\relationship\disease-Ko.csv',sep='\t')

data_3 = pd.concat([data_1 , data_2], ignore_index=True).sort_values(by="disease_index",ascending=False)
data_4 = data_3[['disease_index', 'gene_Index']]

data_4.to_csv(r'E:\Project\PINet\data_set\relationship\processed\disease-gene.csv', sep='\t', index =None)
