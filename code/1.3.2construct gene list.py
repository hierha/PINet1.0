import csv
import numpy as np
import pandas as pd


data_1 = pd.read_csv(r'E:\Project\PINet\data_set\entry\gene from STRING+HVIDB.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\KEGG\processed\K0_genes.txt',sep='\t')


data_3 = pd.merge(data_1,data_2,left_on='KEGG',right_on='ortholog')[['Index','ortholog_gene','Other_ID','GeneName']]
data_3['Other_ID'] = ''
data_3.columns =['Index','KEGG','Other_ID','GeneName']

data_4 = pd.concat([data_1,data_3],ignore_index=True)

data_4.to_csv(r'E:\Project\PINet\data_set\entry\processed\gene.csv', sep='\t', index =None)
