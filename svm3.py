import pickle
import numpy as np

from sklearn import svm

TRAINING_DATA     = "training_data.pickle"
MODEL_DATA		  = "svm_model.pickle"


'''
3) Create & train svm model
'''
print('Loading the training data...')
(X, y) = pickle.load(open(TRAINING_DATA, 'rb'))

model = svm.SVC()

model.fit(X, y)

print('Dumping the SVM model...')
pickle.dump(model, open(MODEL_DATA, 'wb'))