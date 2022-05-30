import csv
with open(r'E:\Project\PINet\evaluate\positive\state\drug-disease.csv','r',encoding='utf-8', newline='') as f1,\
    open(r'E:\Project\PINet\evaluate\negative\state\random_drug_combination.csv','r',encoding='utf-8', newline='') as f2,\
    open(r'E:\Project\PINet\evaluate\ROC\num\state\2.csv','a',encoding='utf-8', newline='') as f3,\
    open(r'E:\Project\PINet\evaluate\ROC\num\state\3.csv','a',encoding='utf-8', newline='') as f4,\
    open(r'E:\Project\PINet\evaluate\ROC\num\state\4.csv','a',encoding='utf-8', newline='') as f5,\
    open(r'E:\Project\PINet\evaluate\ROC\num\state\5.csv','a',encoding='utf-8', newline='') as f6,\
    open(r'E:\Project\PINet\evaluate\ROC\num\state\all.csv','a',encoding='utf-8', newline='') as f7:
    f3writer = csv.writer(f3, delimiter='\t')
    f4writer = csv.writer(f4, delimiter='\t')
    f5writer = csv.writer(f5, delimiter='\t')
    f6writer = csv.writer(f6, delimiter='\t')
    f7writer = csv.writer(f7, delimiter='\t')
    f3writer.writerow(['synergy', 'score'])
    f4writer.writerow(['synergy', 'score'])
    f5writer.writerow(['synergy', 'score'])
    f6writer.writerow(['synergy', 'score'])
    f7writer.writerow(['synergy', 'score'])

    #synergistic drug combination
    count_1 = 0
    for item in csv.reader(f1,delimiter='\t'):
        if count_1 > 0:
            disease_index = item[0]
            drug_num = item[1]
            score = 1/float(item[3])
            synergy = item[6]
            if disease_index in ['3','5','6','9']:
                f7writer.writerow([synergy, score])
                if drug_num == '2':
                    f3writer.writerow([synergy, score])
                elif drug_num == '3':
                    f4writer.writerow([synergy, score])
                elif drug_num == '4':
                    f5writer.writerow([synergy, score])
                else:
                    f6writer.writerow([synergy, score])
        count_1 += 1

    #random drug combination
    count_2 = 0
    for item in csv.reader(f2,delimiter='\t'):
        if count_2 > 0:
            disease_index = item[0]
            drug_num = item[1]
            score = 1/float(item[3])
            synergy = item[6]
            if disease_index in ['3','5','6','9']:
                f7writer.writerow([synergy, score])
                if drug_num == '2':
                    f3writer.writerow([synergy, score])
                elif drug_num == '3':
                    f4writer.writerow([synergy, score])
                elif drug_num == '4':
                    f5writer.writerow([synergy, score])
                else:
                    f6writer.writerow([synergy, score])
        count_2 += 1
