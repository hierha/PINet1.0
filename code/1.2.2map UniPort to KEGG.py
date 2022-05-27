import urllib.parse
import urllib.request

#Construction of UniPort protein collections
protein_list_Uni = []
with open(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to UniPort(STRING).txt', 'r') as file_1:
    for line in file_1.readlines():
        protein = line.split('\t')[1][:-1]
        protein_list_Uni.append(protein)

#UniPort proteins map to KEGG
protein_list_Uni_new = ' '.join(protein_list_Uni)
with open(r'E:\Project\PINet\data_set\database\STRING\processed\UniPort to KEGG(STRING).txt', 'a', encoding='utf-8') as file_2:
    url = 'https://www.uniprot.org/uploadlists/'
    params = {
                    'from': 'ACC+ID',
                    'to': 'KEGG_ID',
                    'format': 'tab',
                    'query': protein_list_Uni_new
                                            }
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read().decode('utf-8')
    file_2.write(response)
