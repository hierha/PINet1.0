import csv

with open(r'E:\Project\PINet\data_set\relationship\path-path.csv','r',newline='') as f1,\
    open(r'E:\Project\PINet\data_set\relationship\processed\path-path.csv','a',newline='') as f2:
    f2writer = csv.writer(f2, delimiter='\t')
    #f2writer.wrtierow(['path_index_x','path_index_y'])
    path_path_set = set()
    for item in csv.reader(f1,delimiter='\t'):
        x = item[0]
        y = item[1]
        a = (x,y)
        b = (y,x)
        if a in path_path_set or b in path_path_set:
            continue
        else:
            f2writer.writerow([x,y])
            path_path_set.add(a)
            path_path_set.add(b)

