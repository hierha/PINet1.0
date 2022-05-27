import numpy as np
import pandas as pd
from PINet import KPEA

f1=r'E:\Project\PINet\RWRer\matrix\drug-gene.npy'
f2=r'E:\Project\PINet\RWRer\matrix\path-gene.npy'
f3=r'E:\Project\PINet\RWRer\matrix\drug-path.npy'
f4=r'E:\Project\PINet\data_set\relationship\processed\drug-path.csv'
KPEA.KEGG_enrichment(f1, f2, f3, f4)

