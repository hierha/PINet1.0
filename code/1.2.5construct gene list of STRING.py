import csv
with open(r'E:\Project\PINet\data_set\database\STRING\processed\protein info of STRING.csv','r',newline='') as f1,\
    open(r'E:\Project\PINet\data_set\database\STRING\processed\gene list of STRING.csv','a',newline='') as f2:
    gene_set = set()
    #recording human genes
    count = 0
    f2writer = csv.writer(f2,delimiter='\t')
    f2writer.writerow(['KEGG_Gene'])
    for item in csv.reader(f1, delimiter='\t'):
        if count > 0:
            KEGG_Gene = item[2]
            if KEGG_Gene in gene_set:
                continue
            else:
                f2writer.writerow([KEGG_Gene])
                gene_set.add(KEGG_Gene)
        count += 1
