import csv
with open(r'E:\Project\PINet\data_set\database\CTD\CTD_genes_diseases.tsv', 'r', newline='', encoding='utf-8') as f1,\
    open(r'E:\Project\PINet\data_set\database\CTD\processed\genes_diseases_formatted.csv', 'a', newline='', encoding='utf-8') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    f2writer.writerow(['GeneSymbol', 'GeneID', 'DiseaseName', 'DiseaseID', 'DirectEvidence', 'InferenceChemicalName','InferenceScore',\
        'OmimIDs', 'PubMedIDs'])
    for item in csv.reader(f1,delimiter='\t'):
        if '#' in item[0]:
            continue
        else:
            DirectEvidence = item[4]
            if DirectEvidence:
                f2writer.writerow(item)
            else:
                continue

