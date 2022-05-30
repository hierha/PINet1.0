import numpy as np
import pandas as pd
import gc
from itertools import combinations
from sklearn.metrics import jaccard_score
from random import sample

def Second_Filter(drug_combination):
    drug_gene = np.load(r'E:\Project\PINet\RWRer\matrix\drug-gene.npy')
    drug_1_index = drug_combination[0]
    drug_2_index = drug_combination[1]
    drug_1 = np.nonzero(drug_gene[drug_1_index])
    drug_2 = np.nonzero(drug_gene[drug_2_index])
    common_target = np.intersect1d(drug_1,drug_2)
    if common_target.size > 0 :
        return True
    else:
        return False

def potential_dc(disease_index, num_of_drug, ftype):
#Access to primary potential drug combinations
    #Extract key disease pathways
    disease_key_path = np.load(r'E:\Project\PINet\RWRer\key_path and key_gene\key_path\{}.npy'.format(disease_index))
    #Extract disease key genes
    disease_key_gene = np.load(r'E:\Project\PINet\RWRer\key_path and key_gene\key_gene\{}.npy'.format(disease_index))
    #Build drug lists based on critical pathways
    path_drug = np.load(r'E:\Project\PINet\RWRer\matrix\drug-path.npy').T
    drug_matrix_path = path_drug[disease_key_path]
    drug_index_path = np.nonzero(drug_matrix_path)[1]
    drug_index_1 = np.unique(drug_index_path)
    #Build drug lists based on key genes
    drug_gene = np.load(r'E:\Project\PINet\RWRer\matrix\drug-gene.npy')
    gene_drug = drug_gene.T
    drug_matrix_gene = gene_drug[disease_key_gene]
    drug_index_gene = np.nonzero(drug_matrix_gene)[1]
    drug_index_2 = np.unique(drug_index_gene)
    #Take the intersection of two drug lists
    drug_index = np.intersect1d(drug_index_1,drug_index_2)
    drug_index_list_1 = drug_index.tolist()

    #Preliminary filter function
    def First_Filter(drug_list):
        nonlocal ftype
        nonlocal drug_gene
        nonlocal disease_index
        new_drug_list = []
        overlap_list = []
        #Determine the threshold
        if ftype == 1:
            disease_gene = np.load(r'E:\Project\PINet\RWRer\key_path and key_gene\key_gene\binary_{}.npy'.format(disease_index))
            for drug in drug_list:
                drug_target = drug_gene[drug]
                overlap = jaccard_score(drug_target,disease_gene)
                overlap_list.append(overlap)
                sorted_overlap = np.sort(np.asarray(overlap_list), axis=0)
                threshold = np.percentile(sorted_overlap,80)
        elif ftype == 0:
            disease_gene = np.load(r'E:\Project\PINet\RWRer\matrix\disease-gene.npy')[disease_index]
            threshold = 0

        #Screening drugs
        for drug in drug_list:
            drug_target = drug_gene[drug]
            overlap = jaccard_score(drug_target,disease_gene)
            if overlap > threshold :
                new_drug_list.append(drug)
            else:
                continue
        return new_drug_list

    #Build a Drug List
    drug_index_list = First_Filter(drug_index_list_1)
    #Build a list of potential drug combinations
    drug_combinations_1 = [drug_combination for drug_combination in combinations(drug_index_list, num_of_drug)]
    num = len(drug_combinations_1)
    print('the num of primary potential drug combination is {}'.format(num))

#Access to secondary potential drug combinations
    condition_ls = []
    drug_combinations_2 = []
    count = 0
    for dc in drug_combinations_1:
        new_dc = [drug_combination for drug_combination in combinations(dc, 2)]
        for item in new_dc:
            if Second_Filter(item):
                condition_ls.append(0)
            else:
                condition_ls.append(1)
        if 0 in condition_ls:
            condition_ls.clear()
        else:
            condition_ls.clear()
            drug_combinations_2.append(dc)
        print('{}/{}'.format(count,num))
        count += 1
        
    print('the num of secondary potential drug combination is {}'.format(len(drug_combinations_2)))

    #clear memory
    for x in list(locals().keys()):
        if x != 'drug_combinations_2':
            del locals()[x]
    gc.collect()
    return drug_combinations_2


