from sklearn import linear_model
from sklearn import svm
import pandas as pd
import pickle

DATA_LABELS_FILE  = "data_labels.csv"
MODEL_DATA		  = "svm_model.pickle"
SAMPLING_NUMBER	  = 50000


print('Loading data_labels pairs...')
raw = pd.read_csv(DATA_LABELS_FILE)


print('Random-sampling '+str(SAMPLING_NUMBER)+' instances...')
sample_raw = raw.sample(SAMPLING_NUMBER)


print('Seperating label from predictors...')
X = sample_raw.drop('label', 1)
y = sample_raw['label']


print('Creating a SVM model and fitting data to the model...')
#model = svm.SVC()
model = linear_model.LogisticRegression()
model.fit(X, y)


print('Saving the SVM model as pickle...')
pickle.dump(model, open(MODEL_DATA, 'wb'))