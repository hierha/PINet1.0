import csv

with open(r'E:\Project\PINet\data_set\database\clinical guidelines\drug-disease.csv','r',encoding='utf-8',newline='') as f1,\
    open(r'E:\Project\PINet\data_set\database\clinical guidelines\processed\drug-disease.csv','a',encoding='utf-8',newline='') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    dc = set()
    for item in csv.reader(f1, delimiter='\t'):
        drug_1,drug_2,drug_3,drug_4,drug_5,disease,evidence = item
        drug_1 = drug_1.capitalize()
        drug_2 = drug_2.capitalize()
        drug_3 = drug_3.capitalize()
        drug_4 = drug_4.capitalize()
        drug_5 = drug_5.capitalize()
        info = [drug_1, drug_2, drug_3, drug_4, drug_5, disease]
        dc_set = frozenset(info)
        if dc_set in dc:
            print(dc_set)
        else:
            f2writer.writerow(info)
            dc.add(dc_set)

