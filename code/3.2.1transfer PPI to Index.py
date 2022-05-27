import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\9606.protein.info.v11.5.txt.inproc',sep=' ') #STRING
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\gene.csv',sep='\t') #gene
data_3 = pd.read_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\PPI_specific_virus.csv',sep='\t') #HVIDB

#transfer STRING to Index
data_4 = pd.merge(data_1 , data_2, how = 'inner',left_on ='protein1', right_on='Other_ID')
data_5 = pd.merge(data_4,data_2,how = 'inner',left_on ='protein2', right_on='Other_ID')
data_6 = data_5[['gene_Index_x','gene_Index_y']]

#transfer STRING to Index
data_7 = pd.merge(data_3 , data_2, how = 'inner',left_on ='Uniprot_human', right_on='Other_ID')
data_8 = pd.merge(data_7 , data_2, how = 'inner',left_on ='Uniprot_virus', right_on='Other_ID')
data_9 = data_8[['gene_Index_x','gene_Index_y']]

data_10 = pd.concat([data_6,data_9],ignore_index=True)
print(data_10)

data_10.to_csv(r'E:\Project\PINet\data_set\relationship\gene-gene.csv', sep='\t', index =None)
