import csv
from PINet import Evaluate_Drug_Combination

def value_to_int(list):
    new_list = []
    for item in list:
        new_list.append(int(float(item)))
    return new_list

def to_set(str):
    ls = str.split(',')
    set_1 = frozenset(value_to_int(ls))
    return set_1

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




with open(r'E:\Project\PINet\evaluate\positive\state\drug-disease.csv', 'r', encoding='utf-8', newline='') as f01:
    #construct positive set
    P = set()
    RP = set()
    count = 0
    for item in csv.reader(f01, delimiter='\t'):
        if count >0:
            drug_num = item[1]
            drug_combination = to_set(item[2])
            if drug_combination in P:
                RP.add(drug_combination)
            else:
                P.add(drug_combination)
        count += 1


with open(r'E:\Project\PINet\evaluate\positive\state\drug-disease.csv', 'r', encoding='utf-8', newline='') as f02,\
    open(r'E:\Project\PINet\evaluate\negative\state\drug combination of different disease.csv', 'a', encoding='utf-8', newline='') as f1:
    f1writer = csv.writer(f1, delimiter='\t')
    f1writer.writerow(['disease_index','drug_num','drug_combination','score_a','score_p','score_pg','synergy'])
    count = 0
    for item in csv.reader(f02, delimiter='\t'):
        if count > 0:
            disease_index = int(item[0])
            drug_num = item[1]
            drug_combination = item[2]
            drug_list = value_to_int(drug_combination.split(','))
            for i in [1,3,4,5,6,7,8,9]:
                if disease_index == i :
                    disease_index_1 = i
                    score_a, score_p, score_pg = Evaluate_Drug_Combination.evaluate_dc(disease_index_1,drug_list)
                    synergy = 1
                    f1writer.writerow([disease_index_1, drug_num, drug_combination, score_a, score_p, score_pg, synergy])
                    print(synergy,score_a)
                else:
                    disease_index_1 = i
                    score_a, score_p, score_pg = Evaluate_Drug_Combination.evaluate_dc(disease_index_1,drug_list)
                    drug_set = to_set(drug_combination)
                    if drug_set in RP and (i == 3 or i ==9):
                        synergy = 1
                    else:
                        synergy = 0
                    print(synergy,score_a)
                    f1writer.writerow([disease_index_1, drug_num, drug_combination, score_a, score_p, score_pg, synergy])
        count += 1




