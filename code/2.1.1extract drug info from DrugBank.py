import xml.etree.ElementTree as ET
import csv

tree = ET.parse(r'E:\Project\PINet\data_set\database\DrugBank\full_database.xml')
root = tree.getroot()

with open(r'E:\Project\PINet\data_set\database\DrugBank\processed\drug info from DrugBank.csv','a',encoding='utf-8',newline='') as file_1:
    spamwrtiter = csv.writer(file_1, delimiter='\t')
    spamwrtiter.writerow(['DrugBank_ID','receptor_ID','drug_name','receptor_name','receptor_source','InChIKey'])
    for drug in root.findall('{http://www.drugbank.ca}drug'):  
        DrugBank_ID = drug.findtext('{http://www.drugbank.ca}drugbank-id')
        drug_name = drug.findtext('{http://www.drugbank.ca}name')
        if drug.attrib['type'] == 'biotech' :
            InChIKey = 'NA'
        else:
            for property in drug.find('{http://www.drugbank.ca}calculated-properties'):
                kind = property.findtext('{http://www.drugbank.ca}kind',default='NA')
                if kind == 'InChIKey':
                    InChIKey = property.findtext('{http://www.drugbank.ca}value')
                    break
                else:
                    InChIKey = 'NA'
        targets = drug.find('{http://www.drugbank.ca}targets')
        enzymes = drug.find('{http://www.drugbank.ca}enzymes')
        carriers = drug.find('{http://www.drugbank.ca}carriers')
        transporters = drug.find('{http://www.drugbank.ca}transporters')
        if targets:
            for receptor in targets:
                receptor_name = receptor.findtext('{http://www.drugbank.ca}name',default='NA')
                polypeptide = receptor.find('{http://www.drugbank.ca}polypeptide')
                if polypeptide:
                    receptor_ID = polypeptide.attrib['id']
                    receptor_source = polypeptide.attrib['source']
                else:
                    receptor_ID = 'NA'
                    receptor_source = 'NA'
                info = [DrugBank_ID,receptor_ID,drug_name,receptor_name,receptor_source,InChIKey]
                spamwrtiter.writerow(info)

        if enzymes:
            for receptor in enzymes:
                receptor_name = receptor.findtext('{http://www.drugbank.ca}name',default='NA')
                polypeptide = receptor.find('{http://www.drugbank.ca}polypeptide')
                if polypeptide:
                    receptor_ID = polypeptide.attrib['id']
                    receptor_source = polypeptide.attrib['source']
                else:
                    receptor_ID = 'NA'
                    receptor_source = 'NA'
                info = [DrugBank_ID,receptor_ID,drug_name,receptor_name,receptor_source,InChIKey]
                spamwrtiter.writerow(info)
        if carriers:
             for receptor in carriers:
                receptor_name = receptor.findtext('{http://www.drugbank.ca}name',default='NA')
                polypeptide = receptor.find('{http://www.drugbank.ca}polypeptide')
                if polypeptide:
                    receptor_ID = polypeptide.attrib['id']
                    receptor_source = polypeptide.attrib['source']
                else:
                    receptor_ID = 'NA'
                    receptor_source = 'NA'
                info = [DrugBank_ID,receptor_ID,drug_name,receptor_name,receptor_source,InChIKey]
                spamwrtiter.writerow(info)
        if transporters:
            for receptor in transporters:
                receptor_name = receptor.findtext('{http://www.drugbank.ca}name',default='NA')
                polypeptide = receptor.find('{http://www.drugbank.ca}polypeptide')
                if polypeptide:
                    receptor_ID = polypeptide.attrib['id']
                    receptor_source = polypeptide.attrib['source']
                else:
                    receptor_ID = 'NA'
                    receptor_source = 'NA'
                info = [DrugBank_ID,receptor_ID,drug_name,receptor_name,receptor_source,InChIKey]
                spamwrtiter.writerow(info)
