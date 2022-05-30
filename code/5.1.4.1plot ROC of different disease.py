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
AUC_1 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\1.csv','AIDS')
AUC_3 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\3.csv','Breast Cancer')
AUC_4 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\4.csv','Atherosclerosis')
AUC_5 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\5.csv','IBD')
AUC_6 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\6.csv','AML')
AUC_7 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\7.csv','Diabete_1')
AUC_8 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\8.csv','Diabete_2')
AUC_9 = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\9.csv','NSCL')
AUC_all = plot_roc(r'E:\Project\PINet\evaluate\ROC\disease\state\all.csv','all')

ax.set_title('ROC of different disease')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')

ax.text(0.5, 0.5, 'PINet1.0', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation='30')

ax.text(0.85, 0.85,'all_AUC = {}'.format(AUC_all))
ax.text(0.85, 0.75,'AIDS_AUC = {}'.format(AUC_1))
ax.text(0.85, 0.65,'Breast Cancer_AUC = {}'.format(AUC_3))
ax.text(0.85, 0.55,'Atherosclerosis_AUC = {}'.format(AUC_4))
ax.text(0.85, 0.45,'IBD_AUC = {}'.format(AUC_5))
ax.text(0.85, 0.35,'AML_AUC = {}'.format(AUC_6))
ax.text(0.85, 0.25,'Diabete_1_AUC = {}'.format(AUC_7))
ax.text(0.85, 0.15,'Diabete_2_AUC = {}'.format(AUC_8))
ax.text(0.85, 0.05,'NSCL_AUC = {}'.format(AUC_9))

ax.legend()
plt.savefig(r'E:\Project\PINet\evaluate\ROC\disease\state\ROC.jpg')
plt.show()

