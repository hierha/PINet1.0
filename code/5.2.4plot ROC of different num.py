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
AUC_2 = plot_roc(r'E:\Project\PINet\evaluate\ROC\num\state\2.csv','2')
AUC_3 = plot_roc(r'E:\Project\PINet\evaluate\ROC\num\state\3.csv','3')
AUC_4 = plot_roc(r'E:\Project\PINet\evaluate\ROC\num\state\4.csv','4')
AUC_5 = plot_roc(r'E:\Project\PINet\evaluate\ROC\num\state\5.csv','5')
AUC_all = plot_roc(r'E:\Project\PINet\evaluate\ROC\num\state\all.csv','all')

ax.set_title('ROC of drug quantity sensitivity')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')

ax.text(0.5, 0.5, 'PINet1.0', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation='30')

ax.text(0.75, 0.75,'all_AUC = {}'.format(AUC_all))
ax.text(0.75, 0.65,'2_AUC = {}'.format(AUC_2))
ax.text(0.75, 0.55,'3_AUC = {}'.format(AUC_3))
ax.text(0.75, 0.45,'4_AUC = {}'.format(AUC_4))
ax.text(0.75, 0.35,'5_AUC = {}'.format(AUC_5))

ax.legend()
plt.savefig(r'E:\Project\PINet\evaluate\ROC\num\state\ROC.jpg')
plt.show()

