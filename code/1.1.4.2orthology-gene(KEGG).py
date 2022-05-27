from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import csv

# 1.Building the KO Collection
KO_set = set()
with open(r'E:\Project\PINet\data_set\database\KEGG\processed\path_ortholog.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        KO = row[1][3:]
        KO_set.add(KO) 
# 2.Iterate the KO collection, get the KO-Genes association, and store the association information
with open(r'E:\Project\PINet\data_set\database\KEGG\processed\K0_genes.txt', 'a', newline='') as file_1:
    for KO in KO_set:
        html = urlopen('http://rest.kegg.jp/link/genes/{}'.format(KO))
        for line in html:
            file_1.write(bytes.decode(line,encoding ='utf-8')) #convert byte string to string
