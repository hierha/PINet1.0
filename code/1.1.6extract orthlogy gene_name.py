from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# 1.Construction of ortholog collections
orthology_set = set()
count = 0
with open(r'E:\Project\PINet\data_set\database\KEGG\processed\specific virus path-orthlogy.csv', 'r',newline='') as file_1:
    for item in csv.reader(file_1,delimiter='\t'):
        if count > 0:
            orthology = item[1][3:]
            orthology_set.add(orthology)
        count += 1


# 2.Iterate the web pages corresponding to the orthologs, extract and store the gene names of the orthologs
with open(r'E:\Project\PINet\data_set\database\KEGG\processed\virus_orthology_name.csv', 'w', newline='') as csvfile_1:
    spamwriter = csv.writer(csvfile_1, delimiter='\t')
    spamwriter.writerow(['orthology','orthology_name'])
    for orthology in orthology_set:
        html = urlopen('https://www.kegg.jp/entry/{}'.format(orthology)) #Web pages for orthologs
        bs = BeautifulSoup(html,'html.parser')
        symbol = bs.find('nobr', string='Symbol')
        if symbol:
            ortholog_tag = symbol.parent.parent #Specify Ortholog Entity
            if ortholog_tag:
                orthology_name = ortholog_tag.find('div').text.replace('\n','').replace('\r','')
                spamwriter.writerow(['ko:{}'.format(orthology),orthology_name])
        else:
            print('{}has no name'.format(orthology))
            
        

