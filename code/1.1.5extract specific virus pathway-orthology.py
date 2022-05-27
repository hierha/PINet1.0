import csv
with open(r'E:\Project\PINet\data_set\entry\disease.txt','r',newline='') as f1,\
    open(r'E:\Project\PINet\data_set\database\KEGG\processed\path_ortholog(KEGG).csv','r',newline='') as f2,\
    open(r'E:\Project\PINet\data_set\database\KEGG\processed\specific virus path-orthlogy.csv','a',newline='') as f3:
    #Build a list of virus-related diseases
    disease_list = []
    for item in f1.readlines():
        info = item.split('\t')
        type = info[4].replace('\n','').replace('\r','')
        path = info[3][5:]
        if type == 'virus':
            disease_list.append(path)
    #Extraction of specific disease-ortholog associations
    f3writer = csv.writer(f3, delimiter='\t')
    f3writer.writerow(['path','orthology'])
        #Extract information about specific diseases
    for item in csv.reader(f2, delimiter='\t'):
        path = item[0]
        orthology = item[1]
        if path in disease_list:
            f3writer.writerow([path,orthology])

