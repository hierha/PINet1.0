import numpy as np
import pandas as pd

data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\CTD\processed\genes_diseases_formatted.csv',sep='\t',\
    dtype={'GeneSymbol':str, 'GeneID':str, 'DiseaseName':str, 'DiseaseID':str, 'DirectEvidence':str, 'InferenceChemicalName':str,'InferenceScore':str,'OmimIDs':str, 'PubMedIDs':str})
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\entry\processed\disease.txt',sep='\t',\
    dtype={'disease_index':str,'di_Symbol':str,'Mesh_ID':str,'Path_KEGG':str,'type':str})

data_3 = pd.merge(data_1 , data_2, how = 'inner',left_on ='DiseaseID', right_on='Mesh_ID')
data_4 = data_3[['di_Symbol','DiseaseID','GeneSymbol','GeneID','disease_index']]
data_5 = data_4.drop_duplicates()

data_5.to_csv(r'E:\Project\PINet\data_set\database\CTD\processed\specific gene-disease.csv', sep='\t', index =None)
