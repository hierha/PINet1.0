import csv

with open(r'E:\Project\PINet\data_set\relationship\gene-gene.csv','r',newline='') as f1,\
    open(r'E:\Project\PINet\data_set\relationship\processed\gene-gene.csv','a',newline='') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    gene_gene_set = set()
    count = 0
    for item in csv.reader(f1,delimiter='\t'):
        x = item[0]
        y = item[1]
        a = (x,y)
        b = (y,x)
        if a in gene_gene_set or b in gene_gene_set:
            continue
        else:
            f2writer.writerow([x,y])
            gene_gene_set.add(a)
            gene_gene_set.add(b)
        print(count)
        count += 1
