from sklearn import linear_model
from sklearn import svm
import pandas as pd
import pickle

DATA_LABELS_FILE  = "data_score.csv"
MODEL_DATA		  = "linear_model.pickle"
SAMPLING_NUMBER	  = 50000


print('Loading data_score pairs...')
raw = pd.read_csv(DATA_LABELS_FILE)


print('Random-sampling '+str(SAMPLING_NUMBER)+' instances...')
sample_raw = raw.sample(SAMPLING_NUMBER)


print('Seperating label from predictors...')
X = sample_raw.drop('score', 1)
y = sample_raw['score']


print('Creating a linear regression model and fitting data to the model...')
model = linear_model.LinearRegression()
model.fit(X, y)


print('Saving the SVM model as pickle...')
pickle.dump(model, open(MODEL_DATA, 'wb'))