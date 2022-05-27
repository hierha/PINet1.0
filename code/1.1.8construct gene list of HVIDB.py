import csv
with open(r'E:\Project\PINet\data_set\database\HVIDB\processed\Human Protein of HVIDB.csv','r',newline='') as f1,\
    open(r'E:\Project\PINet\data_set\database\HVIDB\processed\Virus Protein of HVIDB.csv','r',newline='') as f2,\
    open(r'E:\Project\PINet\data_set\database\HVIDB\processed\gene list of HVIDB.csv','a',newline='') as f3:
    gene_set = set()
    #recording human genes
    count = 0
    f3writer = csv.writer(f3,delimiter='\t')
    f3writer.writerow(['KEGG_Gene'])
    for item in csv.reader(f1, delimiter='\t'):
        if count > 0:
            KEGG_Gene = item[2]
            if KEGG_Gene in gene_set:
                continue
            else:
                f3writer.writerow([KEGG_Gene])
                gene_set.add(KEGG_Gene)
        count += 1
    count = 0
    #record viral genes
    for item in csv.reader(f2, delimiter='\t'):
        if count > 0:
            KEGG_GENE = item[2]
            if KEGG_GENE in gene_set:
                continue
            else:
                f3writer.writerow([KEGG_Gene])
                gene_set.add(KEGG_Gene)
        count += 1