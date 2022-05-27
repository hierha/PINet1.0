import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\KEGG\KEGG_GENES_PATHWAY.txt',sep='\t') #path-gene
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\KEGG\processed\path_ortholog(KEGG).csv',sep='\t') #path-KO
data_3 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\pathway.txt',sep='\t') #path
data_4 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\gene.csv',sep='\t') #gene



#map path-gene
data_5 = pd.merge(data_1, data_4, how = 'inner', left_on ='Gene', right_on='KEGG')
data_6 = pd.merge(data_5, data_3, how = 'inner', left_on ='Pathway', right_on='ID')
data_7 = data_6[['path_index','gene_Index']].drop_duplicates()

#map path-KO
data_8 = pd.merge(data_2 , data_4, how = 'inner',left_on ='Ko', right_on='KEGG')
data_9 = pd.merge(data_8,data_3,how = 'inner',left_on ='Pathway', right_on='ID')
data_10 = data_9[['path_index','gene_Index']].drop_duplicates()

data_11 = pd.concat([data_7,data_10],ignore_index=True)

data_11.to_csv(r'E:\Project\PINet\data_set\relationship\processed\path-gene.csv', sep='\t', index =None)
