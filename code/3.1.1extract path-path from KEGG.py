from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time

# 1.Build a list of pathways
path_list = []
with open(r'E:\Project\PINet\data_set\entry\processed\pathway.txt', 'r') as file_1:
    count = 0
    for line in file_1.readlines():
        if count > 0 :
            pathname = line.split('\t')[1][5:] 
            path_list.append(pathname)
        count += 1
count = 0
sum = len(path_list)
# 2.Iterate the webpage corresponding to the path name, extract and store the associated path information in the path
with open(r'E:\Project\PINet\data_set\database\KEGG\processed\path_map.csv', 'a', newline='') as csvfile_1:
    spamwriter = csv.writer(csvfile_1, delimiter='\t')
    spamwriter.writerow(['path_x','path_y'])
    for path in path_list:
        map1_of_path = []
        map1_of_a_path = set()
        html = urlopen('http://rest.kegg.jp/get/{}/kgml'.format(path)) 
        bs = BeautifulSoup(html,'html.parser')
        map1_tags = bs.find_all('entry', {'type':'map'}) #Specifies the associated pathway entity
        #Get all associated paths in a path
        for map1_tag in map1_tags: 
            map1s = map1_tag['name'] #Get the KEGG ID of the associated pathway entity
            num = map1s.count('map') #Check whether there are multiple associated paths in the map entity
            if num > 1:
                map1s_list = maps.split(' ')
                map1_of_path.extend(map1s_list)
            else:
                map1_of_path.append(map1s)
        #Constructing the pathway-association pathway binary relationship
        for map1 in map1_of_path:
            relation = ('path:{}'.format(path), map1)
            map1_of_a_path.add(relation)
        #save binary relationship
        for relation_list in map1_of_a_path:
           spamwriter.writerow(relation_list)
        print()
        time.sleep(0.1)
        print('{}/{}'.format(count,sum))
        count += 1
