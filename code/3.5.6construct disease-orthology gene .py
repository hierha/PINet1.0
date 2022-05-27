import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\disease.txt',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\KEGG\processed\path_ortholog(KEGG).csv',sep='\t')
data_3 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\gene.csv',sep='\t')

data_4 = pd.merge(data_1 , data_2, how = 'inner',left_on ='Path_KEGG', right_on='Pathway')
data_5 = pd.merge(data_4, data_3, how = 'inner',left_on ='Ko', right_on='KEGG')
data_6 = data_5[['disease_index','gene_Index']]
data_7 = data_6.drop_duplicates().sort_values(by="disease_index",ascending=False)

data_7.to_csv(r'E:\Project\PINet\data_set\relationship\disease-Ko.csv', sep='\t', index =None)
