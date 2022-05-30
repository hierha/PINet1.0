from PINet import RWR
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import gc

def key_path_gene(disease_index):
    #disease state
    disease_state = np.load(r'E:\Project\PINet\RWRer\disease state\{}.npy'.format(disease_index))
    print('extract disease_state')

    #normal state
    normal_state = RWR.RWRer([0],r'E:\Project\PINet\RWRer\normal state\matrix\normal_state-path.npy', r'E:\Project\PINet\RWRer\normal state\matrix\normal_state-gene.npy', r'E:\Project\PINet\RWRer\matrix\path-gene.npy', r'E:\Project\PINet\RWRer\matrix\path-path.npy', r'E:\Project\PINet\RWRer\matrix\gene-gene.npy', 0.5)
    print('capture normal_state')

    #pathway diffusion difference
    pathway_diffusion_difference = (disease_state - normal_state)[:345] #345 is the num of pathway
    print('capture pathway_diffusion_difference between diseas and health')

    #find path_outliers
    sort_path_diffusion = np.sort(pathway_diffusion_difference, axis=0)
    Q1,Q2,Q3 = np.percentile(sort_path_diffusion, (25,50,75))
    k = 1.5
    upper_path = Q3 + k * (Q3-Q1)
    lower_path = Q1 - k * (Q3-Q1)
    path_outliers_index_1 = np.where(pathway_diffusion_difference > upper_path)
    path_outliers_index_2 = np.where(pathway_diffusion_difference < lower_path)
    outliers_index_path = np.union1d(path_outliers_index_1, path_outliers_index_2)

    #gene diffusion difference
    gene_diffusion_difference = (disease_state - normal_state)[345:] #345 is the num of pathway
    print('capture gene_diffusion_difference between diseas and health')

    #find gene_outliers
    sort_gene_diffusion = np.sort(gene_diffusion_difference, axis=0)
    Q11,Q22,Q33 = np.percentile(sort_gene_diffusion, (25,50,75))
    k = 1.5
    upper_gene = Q33 + k * (Q33-Q11)
    lower_gene = Q11 - k * (Q33-Q11)
    gene_outliers_index_1 = np.where(gene_diffusion_difference > upper_gene)
    gene_outliers_index_2 = np.where(gene_diffusion_difference < lower_gene)
    outliers_index_gene = np.union1d(gene_outliers_index_1, gene_outliers_index_2)

    #visualize pathway diffusion difference
    #fig, ax = plt.subplots()
    #ax.boxplot(sort_diffusion)
    #plt.show()
    
    #clear memory
    for x in list(locals().keys()):
        if x != 'outliers_index_gene' and x !='outliers_index_path':
            del locals()[x]
    gc.collect()

    return outliers_index_path, outliers_index_gene