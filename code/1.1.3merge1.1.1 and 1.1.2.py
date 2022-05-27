import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\PPI_specific_virus.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\UniPort(human) to KEGG(HVIDB).txt',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'right',left_on='Uniprot_human',right_on='From')
data_4 = data_3[['Human_GeneName','Uniprot_human','To']]
data_4.columns = ['GeneName_Human','Uniprot_Human','KEGG_Human']

data_5 = data_4.drop_duplicates()
data_5.to_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\Human Protein of HVIDB.csv', sep='\t', index =None)
