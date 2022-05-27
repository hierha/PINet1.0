import urllib.parse
import urllib.request
import csv

with open(r'E:\Project\PINet\data_set\database\BindingDB\processed\UniPort to KEGG.txt','a', encoding='utf-8') as file_2, open(r'E:\Project\PINet\data_set\database\BindingDB\processed\drug-target info.csv', 'r', newline='',encoding='utf-8') as csvfile_1:
    spamreader = csv.reader(csvfile_1, delimiter='\t')
    url = 'https://www.uniprot.org/uploadlists/'
    ids = set()
    for row in spamreader:
        id_1 = row[1]
        ids.add(id_1)
        id_list = ' '.join(list(ids))
    params = {
                    'from': 'ACC+ID',
                    'to': 'KEGG_ID',
                    'format': 'tab',
                    'query': id_list
                                            }
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read().decode('utf-8')
    file_2.write(response)
