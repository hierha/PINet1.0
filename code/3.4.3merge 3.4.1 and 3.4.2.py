import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\BindingDB\processed\drug-target info.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\BindingDB\processed\UniPort to KEGG.txt',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'left',left_on ='UniPort_ID', right_on='From')
data_4 = data_3[['DrugBank_ID','To']]
data_4.columns=['DrugBank_ID','KEGG']
data_5 = data_4.dropna(subset=['KEGG'])

data_5.to_csv(r'E:\Project\PINet\data_set\database\BindingDB\processed\drug info from BindingDB and KEGG.csv', sep='\t', index =None)

