import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\PPI_specific_virus.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\KEGG\processed\virus_orthology_name.csv',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'left',left_on='Virus_GeneName',right_on='orthology_name')
data_4 = data_3[['Virus_GeneName','Uniprot_virus','orthology']]
data_4.columns = ['GeneName_Virus','Uniprot_virus','KEGG_virus']

data_5 = data_4.drop_duplicates().dropna()
data_5.to_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\Virus Protein of HVIDB.csv', sep='\t', index =None)
