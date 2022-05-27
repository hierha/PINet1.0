import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\9606.protein.info.v11.5.txt',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to KEGG(STRING).csv',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'inner',left_on ='string_protein_id', right_on='STRING_ID')
data_4 = data_3[['preferred_name','STRING_ID','KEGG_ID']]
data_4.columns=['GeneName','STRING_ID','KEGG_ID']

data_4.to_csv(r'E:\Project\PINet\data_set\database\STRING\processed\protein info of STRING.csv', sep='\t', index =None)

