import csv

with open(r'E:\Project\PINet\data_set\database\BindingDB\BindingDB_All.tsv','r',newline='',encoding='utf-8') as f1,\
    open(r'E:\Project\PINet\data_set\database\BindingDB\processed\drug-target info.csv','a',newline='',encoding='utf-8') as f2:
    f2writer = csv.writer(f2,delimiter='\t')
    f2writer.writerow(['DrugBank_ID','UniPort_ID'])
    count = 0
    for item in csv.reader(f1, delimiter='\t'):
        if count > 0:
            DrugBank_ID = item[32]
            UniPort_ID = item[41]
            if DrugBank_ID !='' and UniPort_ID != '':
                info = [DrugBank_ID,UniPort_ID]
                f2writer.writerow(info)
        count += 1