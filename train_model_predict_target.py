from sklearn import linear_model
from sklearn import svm
import pandas as pd

from recommendation_worker import *
import multiprocessing
from model import *
from parser import *

DATA_LABELS_FILE  = "data_labels.csv"
TARGET_USERS      = "targetUsers.csv"
TARGET_ITEMS      = "targetItems.csv"
USERS_ITEMS_PICKLE= "users_items.pickle"
USERS_FILE        = "users.csv"
ITEMS_FILE        = "items.csv"
N_WORKERS         = 5
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


print('Creating target sets for items and users...')
target_users = []
for line in open(TARGET_USERS):
    target_users += [int(line.strip())]
target_users = set(target_users)

target_items = []
for line in open(TARGET_ITEMS):
    target_items += [int(line.strip())]


print('Loading the full users and items...')
(header_users, users) = select(USERS_FILE, lambda x: True, build_user, lambda x: int(x[0]))
(header_items, items) = select(ITEMS_FILE, lambda x: True, build_item, lambda x: int(x[0]))


print('Scheduling classification...')
bucket_size = len(target_items) / N_WORKERS
start = 0
jobs = []
for i in range(0, N_WORKERS):
    stop = int(min(len(target_items), start + bucket_size))
    filename = "solution_" + str(i) + ".csv"
    process = multiprocessing.Process(target = classify_worker, args=(target_items[start:stop], target_users, items, users, filename, model))
    jobs.append(process)
    start = stop

for j in jobs:
    j.start()

for j in jobs:
    j.join()