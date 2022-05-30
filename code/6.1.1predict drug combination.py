import numpy as np
from sklearn.metrics import roc_curve, auc
from PINet import Potential_Drug_Combination
from PINet import Evaluate_Drug_Combination
import csv

def find_threshold(file_path):
    array = np.loadtxt(file_path, delimiter='\t',skiprows=1)
    y_true, y_socre = np.array_split(array, 2,axis=1)
    fpr, tpr, thresholds = roc_curve(y_true,y_socre)
    index_fpr = (np.abs(fpr - 0.1)).argmin()
    threshold = 1/thresholds[index_fpr]
    return threshold

def int_to_str(ls):
    new_ls = []
    for item in ls:
        new_item = str(item)
        new_ls.append(new_item)
    return new_ls

#Input parameters
print('Please input the index of disease.')
disease_index = int(input())
print('Please input the number of drug in a drug combination[2-5].')
drug_num = int(input())
print('Please chose the number of potential drug combination. If you want less but fast,input 0; Else input 1')
ftype = int(input())

#Determine the threshold
threshold = find_threshold(r'E:\Project\PINet\evaluate\ROC\num\state\{}.csv'.format(drug_num))
#Access to potential drug combinations
pdc = Potential_Drug_Combination.potential_dc(disease_index,drug_num,ftype)

#Evaluate
with open(r'E:\Project\PINet\predict\{}-{}.csv'.format(disease_index,drug_num),'w',encoding='utf-8',newline='') as f1:
    f1writer = csv.writer(f1, delimiter='\t')
    f1writer.writerow(['drug_combination', 'score', 'is_synergy'])
    count = 0
    for dc in pdc:
        score = Evaluate_Drug_Combination.evaluate_dc(disease_index, dc)[0]
        if score <= threshold:
            is_synergy = 1
        else:
            is_synergy = 0
        new_dc = ','.join(int_to_str(list(dc)))
        if is_synergy == 1:
            f1writer.writerow([new_dc, score, is_synergy])
        print(count)
        count += 1
