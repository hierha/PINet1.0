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

with open(r'E:\Project\PINet\evaluate\random drug combination.csv','r',encoding='utf-8',newline='') as f1,\
    open(r'E:\Project\PINet\evaluate\negative\state\random_drug_combination.csv','a',encoding='utf-8',newline='') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    f2writer.writerow(['disease_index', 'drug_num', 'drug_combination', 'score_a','score_p', 'score_pg', 'synergy'])
    count = 0
    for item in csv.reader(f1, delimiter='\t'):
        if count > 0:
            disease_index = int(item[0])
            drug_num = item[1]
            drug_combination = item[2]
            drug_list = value_to_int(drug_combination.split(','))
            score_a, score_p, score_pg = Evaluate_Drug_Combination.evaluate_dc(disease_index ,drug_list)
            print(count,score_a, score_p, score_pg)
            synergy = 0
            f2writer.writerow([disease_index, drug_num, drug_combination, score_a, score_p, score_pg, synergy])
        count += 1
