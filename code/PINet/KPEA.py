import numpy as np
from scipy import stats
import csv
import math

def KEGG_enrichment(file_object_gene, file_path_gene, out_file_1,out_file_2):
    with open(out_file_2,'a',encoding='utf-8',newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\t')
        spamwriter.writerow(['drug_index','path_index'])
        matrix_1 = np.load(file_object_gene)
        matrix_2 = np.load(file_path_gene)
        drug_num = matrix_1.shape[0]
        path_num = matrix_2.shape[0]
        matrix_3 = np.zeros((drug_num, path_num ))
        for drug in range(drug_num):
            N = np.count_nonzero(matrix_1[drug]) #the gene number of a drug
            gene_index_drug = np.nonzero(matrix_1[drug])
            path_set = set()
            path_index = matrix_2.T[gene_index_drug].nonzero()
            for item in path_index[1]:
                path_set.add(item)
            for path in path_set:
                M = np.count_nonzero(matrix_2[path]) #the gene number of a pathway
                gene_index_path = np.nonzero(matrix_2[path])
                gene_of_drug_in_path = np.intersect1d(gene_index_drug, gene_index_path)
                n = len(gene_of_drug_in_path) #the gene number of a drug in a pathway
                k = math.ceil(0.2 * n)
                p_value = stats.hypergeom.sf(k-1,M,n,N)
                if p_value < 0.05 :
                    matrix_3[drug][path] = 1
                    spamwriter.writerow([drug, path])
            path_set.clear()
        np.save(out_file_1,matrix_3)