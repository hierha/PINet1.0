import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\DrugBank\processed\drug info.csv',sep='\t') #drug-target of DrugBank
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\BindingDB\processed\drug info from BindingDB and KEGG.csv',sep='\t') #drug-target of BindingDB
data_3 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\drug.csv',sep='\t') #drug
data_4 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\gene.csv',sep='\t') #gene

#map DrugBank-KEGG
data_5 = pd.merge(data_1, data_3, how = 'inner', on ='DrugBank_ID')
data_6 = pd.merge(data_5, data_4, how = 'inner', on ='KEGG')
data_7 = data_6[['drug_index','gene_Index']].drop_duplicates()

#map BindingDB-KEGG
data_8 = pd.merge(data_2 , data_3, how = 'inner', on ='DrugBank_ID')
data_9 = pd.merge(data_8, data_4, how = 'inner', on ='KEGG')
data_10 = data_9[['drug_index','gene_Index']].drop_duplicates()

data_11 = pd.concat([data_7,data_10],ignore_index=True)
data_12 = data_11.drop_duplicates()


data_12.to_csv(r'E:\Project\PINet\data_set\relationship\processed\drug-gene.csv', sep='\t', index =None)