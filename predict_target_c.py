from recommendation_worker import *
import pickle
import multiprocessing
from model import *
from parser import *

MODEL_DATA		  = "linear_model.pickle"
TARGET_USERS      = "targetUsers.csv"
TARGET_ITEMS      = "targetItems.csv"
USERS_FILE        = "users.csv"
ITEMS_FILE        = "items.csv"
N_WORKERS         = 5

print('Loading the trained SVM model...')
model = pickle.load(open(MODEL_DATA, 'rb'))


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