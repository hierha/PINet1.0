import csv
from PINet import Evaluate_Drug_Combination

def value_to_int(list):
    new_list = []
    for item in list:
        new_list.append(int(float(item)))
    return new_list

def value_to_str(list):
    new_list = []
    for item in list:
        new_list.append(str(item))
    return new_list

def remove_null(list):
    if '' in list:
        new_list = [i for i in list if i != '']
    else:
        new_list = list
    return new_list

with open(r'E:\Project\PINet\data_set\relationship\drug-disease.csv','r',encoding='utf-8',newline='') as f1,\
    open(r'E:\Project\PINet\evaluate\positive\state\drug-disease.csv','a',encoding='utf-8',newline='') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    f2writer.writerow(['disease_index', 'drug_num', 'drug_combination', 'score_a','score_p', 'score_pg', 'synergy'])
    count = 0
    for item in csv.reader(f1, delimiter='\t'):
        if count > 0:
            new_item = remove_null(item)
            disease_index = int(new_item[-1])
            drug_num = len(new_item)-1
            drug_list = value_to_int(new_item[:-1])
            drug_combination = ','.join(value_to_str(drug_list))
            score_a, score_p, score_pg = Evaluate_Drug_Combination.evaluate_dc(disease_index ,drug_list)
            synergy = 1
            print(count, score_a, score_p, score_pg)
            f2writer.writerow([disease_index, drug_num, drug_combination, score_a, score_p, score_pg, synergy])
        count += 1
