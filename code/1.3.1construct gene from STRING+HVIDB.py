import csv
import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\gene list of HVIDB.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\gene list of STRING.csv',sep='\t')
data_3 = pd.read_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\Human Protein of HVIDB.csv',sep='\t')
data_4 = pd.read_csv(r'E:\Project\PINet\data_set\database\HVIDB\processed\Virus Protein of HVIDB.csv',sep='\t')
data_5 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\protein info of STRING.csv',sep='\t')

#Processing HVIDB data
data_3.columns = ['Gene','Uniprot','KEGG']
data_4.columns = ['Gene','Uniprot','KEGG']
data_6 = pd.concat([data_3,data_4],ignore_index=True)
data_7 = pd.merge(data_1,data_6,how='inner', left_on='KEGG_Gene',right_on='KEGG' )[['KEGG','Uniprot','Gene']]
data_7.columns = ['KEGG','Other_ID','GeneName']

#Process STRING data
data_8 = pd.merge(data_2,data_5,how='inner', left_on='KEGG_Gene',right_on='KEGG_ID' )[['KEGG_ID','STRING_ID','GeneName']]
data_8.columns = ['KEGG','Other_ID','GeneName']

#Merge HVIDB and STRING data
data_9 = pd.concat([data_7,data_8],ignore_index=True).drop_duplicates(ignore_index=True)

#Build a gene list
data_10 = pd.concat([data_1,data_2],ignore_index=True).drop_duplicates(ignore_index=True)
gene_index = pd.DataFrame(np.arange(data_10.shape[0]))
gene_index.columns=['Index']
data_10.insert(loc=0,column='Index',value=gene_index) #插入index列，merge时可以保留index
data_11 = pd.merge(data_10,data_9,how='inner', left_on='KEGG_Gene',right_on='KEGG')[['Index','KEGG','Other_ID','GeneName']]
data_11.columns = ['gene_index','KEGG','Other_ID','GeneName']

data_11.to_csv(r'E:\Project\PINet\data_set\entry\gene from STRING+HVIDB.csv', sep='\t', index =None)
