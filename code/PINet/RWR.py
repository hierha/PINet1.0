import numpy as np
from functools import lru_cache
import sys
sys.setrecursionlimit(20000) #Modify recursion depth

#Build the initial probability function
def InitialProbability(entry_list, Matrix_A, Matrix_B): #entry，entry-a，entry-b
    MATRIX_A = np.load(Matrix_A)
    MATRIX_B = np.load(Matrix_B)
    total_a = MATRIX_A.shape[1] # number of a
    total_b = MATRIX_B.shape[1] # number of b
    index_of_a = np.zeros((1,total_a)) 
    index_of_b = np.zeros((1,total_b)) 
    for entry in entry_list: 
        index_of_a = np.union1d(np.nonzero(MATRIX_A[entry]), index_of_a)
        index_of_b = np.union1d(np.nonzero(MATRIX_B[entry]), index_of_b)
    index_of_a_1 = index_of_a.astype('int64')
    index_of_b_1 = index_of_b.astype('int64')
    sum_a = index_of_a_1.shape[0] 
    sum_b = index_of_b_1.shape[0]
    probability_a = 1/sum_a
    probability_b = 1/sum_b
    InPro_of_a = np.zeros(total_a)
    InPro_of_a[index_of_a_1] = probability_a
    InPro_of_b = np.zeros(total_b)
    InPro_of_b[index_of_b_1] = probability_b
    InPro = 0.5 * np.block([InPro_of_a,InPro_of_b])
    return InPro

#Build homogeneous_small transition matrix function
def homo_TransferMatrix(Matrix):
    MATRIX_1 = np.load(Matrix)
    homo = np.zeros(MATRIX_1.shape)
    x = MATRIX_1.shape[0]
    for i in range(x):
        index_of_xt = np.nonzero(MATRIX_1[i])
        m = np.sum(MATRIX_1[i]) - MATRIX_1[i][i] 
        for j in index_of_xt:
            Probability_of_Transfer = MATRIX_1[i][j]/m
            homo[i][j] = Probability_of_Transfer
        row, col = np.diag_indices_from(MATRIX_1)
        homo[row, col] = 0
    return homo.T

#Build heterogeneous_small transition matrix function
def hetero_TransferMatrix(Matrix):
    MATRIX_2 = np.load(Matrix)

    hetero_1 = np.zeros(MATRIX_2.shape) 
    x,y = MATRIX_2.shape
    for i in range(x):
        index_of_y = np.nonzero(MATRIX_2[i])
        m = np.sum(MATRIX_2[i])
        for j in index_of_y:
            Probability_of_Transfer = MATRIX_2[i][j]/m
            hetero_1[i][j] = Probability_of_Transfer
        M3 = hetero_1.T

    hetero_2 = np.zeros(MATRIX_2.T.shape) 
    a,b = MATRIX_2.T.shape
    for i in range(a):
        index_of_b = np.nonzero(MATRIX_2.T[i])
        m = np.sum(MATRIX_2.T[i])
        for j in index_of_b:
            Probability_of_Transfer = MATRIX_2.T[i][j]/m
            hetero_2[i][j] = Probability_of_Transfer
        M2 = hetero_2.T
    return M2,M3

#Build the transition matrix function
def TransferMatrix(Matrix_xy, Matrix_x, Matrix_y):
    M1 = homo_TransferMatrix(Matrix_x)
    M4 = homo_TransferMatrix(Matrix_y)
    M2,M3 = hetero_TransferMatrix(Matrix_xy)
    M = 0.5 * np.block([[M1,M2],
                        [M3,M4]])
    return M

#Building a restart random walker
def RWRer(entry_list, Matrix_ea, Matrix_eb, Matrix_ab, Matrix_aa, Matrix_bb, r): #r为重启概率
    p_0 = InitialProbability(entry_list, Matrix_ea, Matrix_eb)
    M = TransferMatrix(Matrix_ab, Matrix_aa, Matrix_bb)

    @lru_cache(maxsize=None) 
    def DiffusionProbability(n):
        if n == 0:
            return p_0
        else:
            return (1-r)*np.dot(M,DiffusionProbability(n-1)) + r*p_0

    def RecursionNum():
         condition = True
         n = 1
         while condition:
             a = DiffusionProbability(n)
             b = DiffusionProbability(n+1)
             distance = np.linalg.norm(a-b,ord=2)
             if distance < 0.00000000001:
                 condition = False
             else:
                 n += 1
         return a
    pn = RecursionNum()
    return pn
