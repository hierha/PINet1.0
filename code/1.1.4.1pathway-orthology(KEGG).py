from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time

# 1.Build a list of pathways
path_list = []
count = 0
with open(r'E:\Project\PINet\data_set\entry\processed\pathway.txt', 'r') as file_1:
        for line in file_1.readlines():
            if count > 0 :
                pathname = line.split('\t')[1][5:] 
                path_list.append(pathname)
            count += 1
sum = len(path_list)
count = 0
# 2.Iterate the webpage corresponding to the path name, extract and store the associated path information in the path
with open(r'E:\Project\PINet\data_set\database\KEGG\processed\path_ortholog(KEGG).csv', 'w', newline='') as csvfile_1:
    spamwriter = csv.writer(csvfile_1, delimiter='\t')
    spamwriter.writerow(['Pathway','Ko'])
    for path in path_list:
        ortholog_of_path = []
        ortholog_of_a_path = set()
        html = urlopen('http://rest.kegg.jp/get/{}/kgml'.format(path)) 
        bs = BeautifulSoup(html,'html.parser')
        ortholog_tags = bs.find_all('entry', {'type':'ortholog'}) #Specify orthologous genes
        #Get all orthologous genes in a pathway
        if ortholog_tags:
            for ortholog_tag in ortholog_tags: 
                orthologs = ortholog_tag['name'] #Get the KEGG ID of the orthologous gene
                num = orthologs.count('ko') #To examine whether there are multiple subgenes in orthologous genes
                if num > 1:
                    orthologs_list = orthologs.split(' ')
                    ortholog_of_path.extend(orthologs_list)
                else:
                    ortholog_of_path.append(orthologs)
            #Construction of pathway-orthologous gene binary relationships
            for ortholog in ortholog_of_path:
                relation = ('path:{}'.format(path), ortholog)
                ortholog_of_a_path.add(relation)
            #store binary relations
            for relation_list in ortholog_of_a_path:
                spamwriter.writerow(relation_list)
        print('{}/{}'.format(count,sum))
        count += 1
        time.sleep(0.1)

