import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\CTD\processed\GeneBank to Uniport.txt',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\CTD\processed\Uniport to KEGG.txt',sep='\t')
data_3 = pd.read_csv(r'E:\Project\PINet\data_set\database\CTD\processed\specific gene-disease.csv',sep='\t')
data_4 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\gene.csv',sep='\t')

data_1.columns=['NCBI', 'UniProt']
data_2.columns=['UniProt', 'KEGG']

data_5 = pd.merge(data_1 , data_2, how = 'inner',on ='UniProt')
data_6 = pd.merge(data_3, data_5, how = 'inner',left_on ='GeneID', right_on='NCBI')
data_7 = pd.merge(data_6, data_4, how = 'inner',on ='KEGG')
data_8 = data_7[['disease_index','gene_Index']]
data_9 = data_8.drop_duplicates().sort_values(by="disease_index",ascending=False)

data_9.to_csv(r'E:\Project\PINet\data_set\relationship\disease-gene from CTD.csv', sep='\t', index =None)


