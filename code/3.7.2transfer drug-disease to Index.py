import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\clinical guidelines\processed\drug-disease.csv',sep='\t') #drug-disease
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\drug.csv',sep='\t',dtype={'drug_index':int}) #drug
data_3 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\disease.txt',sep='\t',dtype={'gene_Index':int}) #disease

data_4 = pd.merge(data_1, data_3, how = 'inner', left_on ='disease',right_on='di_Symbol')
data_5 = data_4[['Drug_1','Drug_2','Drug_3','Drug_4','Drug_5','disease_index']].drop_duplicates()
data_6 = pd.merge(data_5, data_2, how = 'left', left_on ='Drug_1',right_on='drug_name')
data_7 = pd.merge(data_6, data_2, how = 'left', left_on ='Drug_2',right_on='drug_name')
data_7.columns = ['Drug_1', 'Drug_2', 'Drug_3', 'Drug_4', 'Drug_5', 'disease_index',
       'Drug_1_index', 'DrugBank_ID_x', 'drug_name_x', 'Drug_2_index',
       'DrugBank_ID_y', 'drug_name_y']
data_8 = pd.merge(data_7, data_2, how = 'left', left_on ='Drug_3',right_on='drug_name')
data_9 = pd.merge(data_8, data_2, how = 'left', left_on ='Drug_4',right_on='drug_name')
data_9.columns =['Drug_1', 'Drug_2', 'Drug_3', 'Drug_4', 'Drug_5', 'disease_index',
       'Drug_1_index', 'DrugBank_ID_x', 'drug_name_x', 'Drug_2_index',
       'DrugBank_ID_y', 'drug_name_y', 'Drug_3_index', 'DrugBank_ID_x',
       'drug_name_x', 'Drug_4_index', 'DrugBank_ID_y', 'drug_name_y']
data_10 = pd.merge(data_9, data_2, how = 'left', left_on ='Drug_5',right_on='drug_name')
data_10.columns = ['Drug_1', 'Drug_2', 'Drug_3', 'Drug_4', 'Drug_5', 'disease_index',
       'Drug_1_index', 'DrugBank_ID_x', 'drug_name_x', 'Drug_2_index',
       'DrugBank_ID_y', 'drug_name_y', 'Drug_3_index', 'DrugBank_ID_x',
       'drug_name_x', 'Drug_4_index', 'DrugBank_ID_y', 'drug_name_y',
       'Drug_5_index', 'DrugBank_ID', 'drug_name']
data_11 =data_10[['Drug_1_index','Drug_2_index', 'Drug_3_index', 'Drug_4_index','Drug_5_index','disease_index']]

data_11.to_csv(r'E:\Project\PINet\data_set\relationship\drug-disease.csv', sep='\t', index =None)

