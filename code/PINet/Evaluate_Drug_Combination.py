from PINet import RWR
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import gc

def evaluate_dc(disease_index, drug_combination):
    #disease state
    disease_state = np.load(r'E:\Project\PINet\RWRer\disease state\{}.npy'.format(disease_index))
    
    #drug state
    drug_state = RWR.RWRer(drug_combination,r'E:\Project\PINet\RWRer\matrix\drug-path.npy',r'E:\Project\PINet\RWRer\matrix\drug-gene.npy', r'E:\Project\PINet\RWRer\matrix\path-gene.npy', r'E:\Project\PINet\RWRer\matrix\path-path.npy', r'E:\Project\PINet\RWRer\matrix\gene-gene.npy', 0.5)
    
    #key path
    key_path_index = np.load(r'E:\Project\PINet\RWRer\key_path and key_gene\key_path\{}.npy'.format(disease_index))
    
    #key gene
    key_gene_index = np.load(r'E:\Project\PINet\RWRer\key_path and key_gene\key_gene\{}.npy'.format(disease_index))
    
    #distance
        #all
    distance_all = np.linalg.norm(disease_state - drug_state, ord=2)
        #path
    disease_state_path = disease_state[:345]
    drug_state_path = drug_state[:345]
    distance_path = np.linalg.norm(disease_state_path[key_path_index] - drug_state_path[key_path_index], ord=2)
        #path+gene
    disease_state_gene = disease_state[345:]
    drug_state_gene = drug_state[345:]
    disease_key_path_gene = np.concatenate((disease_state_path[key_path_index], disease_state_gene[key_gene_index]))
    drug_key_path_gene = np.concatenate((drug_state_path[key_path_index], drug_state_gene[key_gene_index]))
    distance_path_gene = np.linalg.norm(disease_key_path_gene - drug_key_path_gene, ord=2)
    #clear memory
    for x in list(locals().keys()):
        if x != 'distance_path' and x != 'distance_all' and x != 'distance_path_gene':
            del locals()[x]
    gc.collect()
    return distance_all,distance_path,distance_path_gene
