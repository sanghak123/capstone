import numpy as np
import csv
import pickle

from model import *
from parser import *

print(" --- Recsys Challenge 2017 Baseline --- ")

USERS_FILE        = "users.csv"
ITEMS_FILE        = "items.csv"
INTERACTIONS_FILE = "interactions.csv"
DATA_LABELS       = "data_labels.csv"
USERS_ITEMS_PICKLE= "users_items.pickle"


print('Parsing the challenge data, excluding all impressions...')
(header_users, users) = select(USERS_FILE, lambda x: True, build_user, lambda x: int(x[0]))
(header_items, items) = select(ITEMS_FILE, lambda x: True, build_item, lambda x: int(x[0]))
builder = InteractionBuilder(users, items)
(header_interactions, interactions) = select(
    INTERACTIONS_FILE,
    lambda x: x[2] != '0',  
    builder.build_interaction,
    lambda x: (int(x[0]), int(x[1])) 
)


print('Saving the users_items in pickle...')
pickle.dump((users, items), open(USERS_ITEMS_PICKLE, 'wb'))


print('Build recsys training data...')
data_titles = ['title_match', 'clevel_match', 'indus_match', 'discipline_match', 'country_match', 'region_match']
label_title = ['label']
titles = data_titles + label_title

with open(DATA_LABELS, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(titles)
    i = 0
    for key in interactions.keys():
        i += 1
        if i % 10000 == 0:
            print('line #'+str(i)+' is being read.')
        writer.writerow(interactions[key].features()+[interactions[key].label()])