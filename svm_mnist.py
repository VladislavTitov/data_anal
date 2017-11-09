from sklearn import datasets, svm, metrics
from sklearn.linear_model.logistic import LogisticRegression as lg

digits = datasets.load_digits()

images_and_labels = list(zip(digits.images, digits.target))

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

svm = svm.SVC(gamma=0.001)
logreg = lg()

svm.fit(data[:n_samples // 2], digits.target[:n_samples // 2])
logreg.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

expected = digits.target[n_samples // 2:]
pred_svm = svm.predict(data[n_samples // 2:])
pred_log = logreg.predict(data[n_samples // 2:])

print("SVM accuracy : %s" % metrics.accuracy_score(expected, pred_svm, normalize=True))
print("LogReg accuracy : %s" % metrics.accuracy_score(expected, pred_log, normalize=True))
