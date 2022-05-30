import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc

def plot_roc(file_path, num_label):
    array = np.loadtxt(file_path, delimiter='\t',skiprows=1)
    y_true, y_socre = np.array_split(array, 2,axis=1)
    fpr, tpr, thresholds = roc_curve(y_true,y_socre)
    value = round(auc(fpr,tpr), 3)
    ax.plot(fpr, tpr, linewidth=2.0, label=num_label)
    return value

fig, ax = plt.subplots(1,1)

AUC_1 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\3.csv','Breast Cancer')
AUC_2 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\5.csv','IBD')
AUC_3 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\6.csv','AML')
AUC_4 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\9.csv','NSCL')

ax.set_title('ROC of high sensitivity disease')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')

ax.text(0.5, 0.5, 'PINet1.0', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation='30')

ax.text(0.55, 0.55,'Breast Cancer_AUC = {}'.format(AUC_1))
ax.text(0.55, 0.45,'IBD_AUC = {}'.format(AUC_2))
ax.text(0.55, 0.35,'AML_AUC = {}'.format(AUC_3))
ax.text(0.55, 0.25,'NSCL_AUC = {}'.format(AUC_4))



ax.legend()
plt.savefig(r'E:\Project\PINet\evaluate\ROC\disease\state\ROC(high).jpg')
plt.show()


