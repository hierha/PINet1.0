import numpy as np
import pandas as pd
from PINet import association_matrix

path_num = 345
gene_num = 18532
drug_num = 6259
disease_num = 10

#path-path
association_matrix.association_matrix(path_num, path_num, r'E:\Project\PINet\data_set\relationship\processed\path-path.csv', r'E:\Project\PINet\RWRer\matrix\path-path.npy')
print('path-path is finished')

#gene-gene
association_matrix.association_matrix(gene_num, gene_num, r'E:\Project\PINet\data_set\relationship\processed\gene-gene.csv', r'E:\Project\PINet\RWRer\matrix\gene-gene.npy')
print('gene-gene is finished')

#path_gene
association_matrix.association_matrix(path_num, gene_num, r'E:\Project\PINet\data_set\relationship\processed\path-gene.csv', r'E:\Project\PINet\RWRer\matrix\path-gene.npy')
print('path-gene is finished')

#drug_gene
association_matrix.association_matrix(drug_num, gene_num, r'E:\Project\PINet\data_set\relationship\processed\drug-gene.csv', r'E:\Project\PINet\RWRer\matrix\drug-gene.npy')
print('drug-gene is finished')

#disease_gene
association_matrix.association_matrix(disease_num, gene_num, r'E:\Project\PINet\data_set\relationship\processed\disease-gene.csv', r'E:\Project\PINet\RWRer\matrix\disease-gene.npy')
print('disease-gene is finished')

#disease_path
association_matrix.association_matrix(disease_num, path_num, r'E:\Project\PINet\data_set\relationship\processed\disease-path from KEGG.csv', r'E:\Project\PINet\RWRer\matrix\disease-path.npy')
print('disease-path is finished')