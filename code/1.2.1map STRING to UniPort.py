import urllib.parse
import urllib.request

#Construction of STRING protein collections
protein_list = []
with open(r'E:\Project\PINet\data_set\database\STRING\9606.protein.info.v11.5.txt', 'r') as file_1:
    for line in file_1.readlines():
        protein = line.split('\t')[0]
        protein_list.append(protein)

#Mapping of STRING proteins to UniPort
protein_list_new = ' '.join(protein_list)
with open(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to UniPort(STRING).txt', 'a', encoding='utf-8') as file_2:
    url = 'https://www.uniprot.org/uploadlists/'
    params = {
                    'from': 'STRING_ID',
                    'to': 'ACC',
                    'format': 'tab',
                    'query': protein_list_new
                                            }
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read().decode('utf-8')
    file_2.write(response)

