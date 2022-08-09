import numpy as np
import pandas as pd

#读取文件，形成dataFrame格式
data_1 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to UniPort(STRING).csv',sep='\t')
data_2 = pd.read_csv(r'E:\Project\PINet\data_set\database\STRING\processed\UniPort to KEGG(STRING).csv',sep='\t')

#合并数据
data_3 = pd.merge(data_1 , data_2, how = 'inner',on ='UniProt_ID',)



#储存数据
data_3.to_csv(r'E:\Project\PINet\data_set\database\STRING\processed\STRING to KEGG(STRING).csv', sep='\t', index =None)
