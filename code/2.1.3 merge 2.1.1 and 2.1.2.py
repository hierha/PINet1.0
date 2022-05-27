import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\DrugBank\processed\drug info from DrugBank.csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\DrugBank\processed\UniPort to KEGG.txt',sep='\t')

data_3 = pd.merge(data_1 , data_2, how = 'left',left_on ='receptor_ID', right_on='From')
data_4 = data_3[['DrugBank_ID','receptor_ID','To','drug_name','receptor_name','receptor_source','InChIKey']]
data_4.columns=['DrugBank_ID','receptor_ID','KEGG','drug_name','receptor_name','receptor_source','InChIKey']
data_4.dropna(subset=['KEGG'],inplace=True)

data_4.to_csv(r'E:\Project\PINet\data_set\database\DrugBank\processed\drug info from Drugbank and KEGG.csv', sep='\t', index =None)

