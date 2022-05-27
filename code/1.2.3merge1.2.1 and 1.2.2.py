import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to UniPort(STRING).txt',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\UniPort to KEGG(STRING).txt',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'inner',left_on ='To', right_on='From')
data_4 = data_3[['From_x','To_y']]
data_4.columns=['STRING_ID','KEGG_ID']

data_4.to_csv(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to KEGG(STRING).csv', sep='\t', index =None)

