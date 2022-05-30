import numpy as np
import pandas as pd

def int_list(ls):
    new_ls = []
    for item in ls:
        new_ls.append(int(item))
    return new_ls


print('please input the name of file from 6.1.1')
file_name = input()
with open(r'E:\Project\PINet\predict\{}.csv'.format(file_name),'r',encoding='utf-8') as f1:
    drug_combinations = []
    for line in f1.readlines()[1:]:
        drug_combination = line.split('\t')[0].split(',')
        drug_combinations.append(int_list(drug_combination))


drug_combinations_pd= pd.DataFrame(np.array(drug_combinations))
drug_combinations_pd.columns = ['drug_1','drug_2'] 

drug_info = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\drug.csv',sep='\t')
data_1 = pd.merge(drug_combinations_pd , drug_info, how = 'left',left_on ='drug_1', right_on='drug_index')
data_2 = pd.merge(data_1, drug_info, how = 'left',left_on ='drug_2', right_on='drug_index')
data_3 = data_2[['drug_name_x','drug_name_y']]

data_3.to_csv(r'E:\Project\PINet\predict\processed\{}.csv'.format(file_name), sep='\t', index =None)

