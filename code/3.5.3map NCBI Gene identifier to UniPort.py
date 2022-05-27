import urllib.parse
import urllib.request
import csv

with open(r'E:\Project\PINet\data_set\database\CTD\processed\GeneBank to Uniport.txt','a', encoding='utf-8') as file_2, open(r'E:\Project\PINet\data_set\database\CTD\processed\specific gene-disease.csv', 'r', newline='',encoding='utf-8') as csvfile_1:
    spamreader = csv.reader(csvfile_1, delimiter='\t')
    url = 'https://www.uniprot.org/uploadlists/'
    ids = set()
    for row in spamreader:
        id_1 = row[4]
        ids.add(id_1)
    print(len(ids))
    id_list = ' '.join(list(ids))
    print('The list construction is completed, the mapping starts, please be patient')
    params = {
                    'from': 'P_ENTREZGENEID',
                    'to': 'ACC',
                    'format': 'tab',
                    'query': id_list
                                            }
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read().decode('utf-8')
    file_2.write(response)

