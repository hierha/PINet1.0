import urllib.parse
import urllib.request
import csv

with open(r'E:\Project\PINet\data_set\database\CTD\processed\Uniport to KEGG.txt','a', encoding='utf-8') as file_2, open(r'E:\Project\PINet\data_set\database\CTD\processed\GeneBank to Uniport.txt', 'r', newline='',encoding='utf-8') as file_1:
    url = 'https://www.uniprot.org/uploadlists/'
    ids = set()
    for item in file_1.readlines():
        id = item.split('\t')[1].replace('\n','').replace('\r','')
        ids.add(id)
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
