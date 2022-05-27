import csv
import re

file_1 = open(r'E:\Project\PINet\data_set\database\HVIDB\hvidb.txt', 'r', newline='')
#set virus type
influenza = re.compile(r'H\dN\d')
virus_condition = ('SARS-CoV-2', 'HIV-1')

with open(r'E:\Project\PINet\data_set\database\HVIDB\processed\PPI_specific_virus.csv', 'a', newline='') as csv_file:
    spamwriter = csv.writer(csv_file, delimiter='\t')
    spamwriter.writerow(['Uniprot_human','Uniprot_virus','short','Human_GeneName','Virus_GeneName'])
    for item in file_1.readlines():
        info = item.split('\t')
        Uniprot_human = info[0]
        Uniprot_virus = info[1]
        short = info[13]
        Human_GeneName = info[17]
        Virus_GeneName = info[20]
        #Determine whether the virus meets the requirements
        if short in virus_condition or re.match(influenza,short) : 
            #keep the first human gene name
            if ';' in Human_GeneName:
                Human_GeneName = Human_GeneName.split(';')[0]
            #keep the first virus gene name
            if ';' in Virus_GeneName:
                Virus_GeneName = Virus_GeneName.split(';')[0]
            #Replace the NA of influenza virus with neuraminidase
            if short != 'HIV-1' and Virus_GeneName == 'NA':
                Virus_GeneName = 'neuraminidase'
            write_info = [Uniprot_human,Uniprot_virus,short,Human_GeneName,Virus_GeneName]
            spamwriter.writerow(write_info)

        