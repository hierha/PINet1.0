import csv

with open(r'E:\Project\PINet\data_set\entry\processed\gene.csv', 'r',  encoding='utf-8',newline='') as f1,\
    open(r'E:\Project\PINet\RWRer\normal state\normal state-gene.csv', 'a', encoding='utf-8', newline='') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    f2writer.writerow(['gene_Index'])
    gene_set = set()
    for item in csv.reader(f1, delimiter='\t'):
        gene_Index = item[0]
        KEGG = item[1]
        if 'hsa:' in KEGG:
            if gene_Index in gene_set:
                continue
            else:
                f2writer.writerow([gene_Index])
                gene_set.add(gene_Index)
        else:
            continue
