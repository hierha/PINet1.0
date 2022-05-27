import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\DrugBank\processed\drug info.csv',sep='\t')

data_2 = data_1[['DrugBank_ID','drug_name']]
data_3 = data_2.drop_duplicates()
data_4 = data_3.reset_index(drop=True)

data_4.to_csv(r'E:\Project\PINet\data_set\entry\processed\drug.csv', sep='\t', index =True,index_label='drug_index')
