import csv
import random
import pandas as pd

def value_to_int(list):
    new_list = []
    for item in list:
        new_list.append(int(item))
    return new_list

def value_to_str(list):
    new_list = []
    for item in list:
        new_list.append(str(item))
    return new_list

def to_set(str):
    ls = str.split(',')
    set_1 = frozenset(value_to_int(ls))
    return set_1

def ran_drug_combination(drug_num, drugcom_num, positive_set):
    ran_dc_ls = random.sample(range(int(drug_num)),int(drugcom_num))
    ran_dc_set = frozenset(ran_dc_ls)
    while ran_dc_set in positive_set:
        ran_dc_ls = random.sample(range(int(drug_num)),int(drugcom_num))
        ran_dc_set = frozenset(ran_dc_ls)
    return list(ran_dc_set)

with open(r'E:\Project\PINet\evaluate\positive\state\drug-disease.csv', 'r', encoding='utf-8', newline='') as f1:
    #construct positive set
    P2 = set()
    P3 = set()
    P4 = set()
    P5 = set()
    count = 0
    for item in csv.reader(f1, delimiter='\t'):
        if count >0:
            drug_num = item[1]
            drug_combination = to_set(item[2])
            if drug_num == '2':
                P2.add(drug_combination)
            elif drug_num == '3':
                P3.add(drug_combination)
            elif drug_num == '4':
                P4.add(drug_combination)
            else:
                P5.add(drug_combination)
        count += 1
    P_all = P2 | P3 | P4 | P5

dataframe_1 = pd.read_csv(r'E:\Project\PINet\evaluate\positive\state\drug-disease.csv', sep='\t')
with open(r'E:\Project\PINet\evaluate\random drug combination.csv','a',encoding='utf-8', newline='') as f2:
    #construct negative set
    f2writer = csv.writer(f2, delimiter='\t')
    f2writer.writerow(['disease_index', 'drug_num', 'drug_combination'])
    count_1 = 0

    while count_1 < 29 :
        for row in dataframe_1.itertuples(index=False, name=None):
            disease_index = row[0]
            drug_num = row[1]
            drug_combination_list = ran_drug_combination(6259,drug_num,P_all)
            drug_combination = ','.join(value_to_str(drug_combination_list))
            f2writer.writerow([disease_index, drug_num, drug_combination])
        count_1 += 1


