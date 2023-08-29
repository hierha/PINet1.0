import csv

with open(r'E:\Project\PINet\data_set\entry\processed\pathway.txt', 'r',  encoding='utf-8') as f1,\
    open(r'E:\Project\PINet\RWRer\normal state\normal state-path.csv', 'a', encoding='utf-8', newline='') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    #f2writer.writerow(['path_index'])
    for item in f1.readlines():
        path_index = item.split('\t')[0]
        is_disease = item.split('\t')[3].replace('\n','').replace('\r','')
        if is_disease == '1':
            continue
        else:
            f2writer.writerow([path_index])
