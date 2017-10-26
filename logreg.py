import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression as lr
import sklearn.datasets as ds
from functools import reduce
from math import fabs

def predict(X, Y):
    train_size = round(len(X) * 0.8)
    test_size = len(X) - train_size

    train_X = X[:train_size]
    test_X = X[test_size:]
    train_Y = Y[:train_size]
    test_Y = Y[test_size:]

    svm = SVC(kernel='linear')
    logreg = lr()

    svm.fit(train_X, train_Y)
    logreg.fit(train_X, train_Y)

    pred_svm = svm.predict(test_X)
    pred_log = logreg.predict(test_X)
    return pred_svm, pred_log, test_Y

def compare(array1, array2):
    return reduce((lambda x, y: x + y), [fabs(a - b) for a, b in zip(array1, array2)])


X, Y = ds.make_classification(n_features=2, n_redundant=0, n_informative=1,
                             n_clusters_per_class=1)
pred_svm, pred_log, test_Y = predict(X, Y)
a = compare(test_Y, pred_svm)
b = compare(test_Y, pred_log)
print('Точность SVM (make_classification): ' + str(a) + ' ошибок из ' + str(len(test_Y)))
print('Точность LogReg (make_classification): ' + str(b) + ' ошибок из ' + str(len(test_Y)))

print()

X1, Y1 = ds.make_gaussian_quantiles(n_features=2, n_classes=2)
pred_svm, pred_log, test_Y = predict(X, Y)
a = compare(test_Y, pred_svm)
b = compare(test_Y, pred_log)
print('Точность SVM (make_gaussian_quantiles): ' + str(a) + ' ошибок из ' + str(len(test_Y)))
print('Точность LogReg (make_gaussian_quantiles): ' + str(b) + ' ошибок из ' + str(len(test_Y)))