import numpy as np

from model import *
from parser import *

import pickle

from sklearn import svm

print(" --- Recsys Challenge 2017 Baseline --- ")

N_WORKERS         = 5
USERS_FILE        = "users.csv"
ITEMS_FILE        = "items.csv"
INTERACTIONS_FILE = "interactions.csv"
TRAINING_DATA     = "training_data.pickle"
SAMPLING_NUMBER   = 100

'''
1) Parse the challenge data, exclude all impressions
   Exclude all impressions
'''
(header_users, users) = select(USERS_FILE, lambda x: True, build_user, lambda x: int(x[0]))
(header_items, items) = select(ITEMS_FILE, lambda x: True, build_item, lambda x: int(x[0]))

builder = InteractionBuilder(users, items)
(header_interactions, interactions) = select(
    INTERACTIONS_FILE,
    lambda x: x[2] != '0',  
    builder.build_interaction,
    lambda x: (int(x[0]), int(x[1])) 
)


'''
2) Build recsys training data
'''
data    = np.array([interactions[key].features() for key in interactions.keys()])
labels  = np.array([interactions[key].label() for key in interactions.keys()])

print(full_data.size)
print(full_labels.size)

'''
3) Create & train svm model
'''
print('Creating & training the SVM model...')

model = svm.SVC()

model.fit(data, labels)

print('Dumping the SVM model...')
pickle.dump(model, open(MODEL_DATA, 'wb'))