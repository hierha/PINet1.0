import csv
with open(r'E:\Project\PINet\evaluate\negative\state\drug combination of different disease.csv','r',encoding='utf-8', newline='') as file1,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\1.csv','a',encoding='utf-8', newline='') as f1,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\3.csv','a',encoding='utf-8', newline='') as f3,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\4.csv','a',encoding='utf-8', newline='') as f4,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\5.csv','a',encoding='utf-8', newline='') as f5,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\6.csv','a',encoding='utf-8', newline='') as f6,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\7.csv','a',encoding='utf-8', newline='') as f7,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\8.csv','a',encoding='utf-8', newline='') as f8,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\9.csv','a',encoding='utf-8', newline='') as f9,\
    open(r'E:\Project\PINet\evaluate\ROC\disease\state\all.csv','a',encoding='utf-8', newline='') as f10:
    f1writer = csv.writer(f1, delimiter='\t')
    f3writer = csv.writer(f3, delimiter='\t')
    f4writer = csv.writer(f4, delimiter='\t')
    f5writer = csv.writer(f5, delimiter='\t')
    f6writer = csv.writer(f6, delimiter='\t')
    f7writer = csv.writer(f7, delimiter='\t')
    f8writer = csv.writer(f8, delimiter='\t')
    f9writer = csv.writer(f9, delimiter='\t')
    f10writer = csv.writer(f10, delimiter='\t')

    f1writer.writerow(['synergy', 'score'])
    f3writer.writerow(['synergy', 'score'])
    f4writer.writerow(['synergy', 'score'])
    f5writer.writerow(['synergy', 'score'])
    f6writer.writerow(['synergy', 'score'])
    f7writer.writerow(['synergy', 'score'])
    f8writer.writerow(['synergy', 'score'])
    f9writer.writerow(['synergy', 'score'])
    f10writer.writerow(['synergy', 'score'])

    count_1 = 0
    for item in csv.reader(file1,delimiter='\t'):
        if count_1 > 0:
            disease_index = item[0]
            score = 1/float(item[3])
            synergy = item[6]
            f10writer.writerow([synergy, score])
            if disease_index == '1':
                f1writer.writerow([synergy, score])
            elif disease_index == '3':
                f3writer.writerow([synergy, score])
            elif disease_index == '4':
                f4writer.writerow([synergy, score])
            elif disease_index == '5':
                f5writer.writerow([synergy, score])
            elif disease_index == '6':
                f6writer.writerow([synergy, score])
            elif disease_index == '7':
                f7writer.writerow([synergy, score])
            elif disease_index == '8':
                f8writer.writerow([synergy, score])
            else:
                f9writer.writerow([synergy, score])
        count_1 += 1

