import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to UniPort(STRING).csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\UniPort to KEGG(STRING).csv',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'inner',on ='UniProt_ID',)

data_3.to_csv(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to KEGG(STRING).csv', sep='\t', index =None)
