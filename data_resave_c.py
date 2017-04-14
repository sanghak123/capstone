import numpy as np
import csv
import pickle

from model import *
from parser import *

print(" --- Recsys Challenge 2017 Baseline --- ")

USERS_FILE        = "users.csv"
ITEMS_FILE        = "items.csv"
INTER_COUNT_FILE  = "interactions_count.csv"
DATA_SCORE        = "data_score.csv"
USERS_ITEMS_PICKLE= "users_items.pickle"


print('Parsing the challenge data, excluding all impressions...')
(header_users, users) = select(USERS_FILE, lambda x: True, build_user, lambda x: int(x[0]))
(header_items, items) = select(ITEMS_FILE, lambda x: True, build_item, lambda x: int(x[0]))
builder = InteractionCountBuilder(users, items)
(header_inter_count, inter_count) = select(
    INTER_COUNT_FILE,
    lambda x: True,  
    builder.build_interaction,
    lambda x: (int(x[0]), int(x[1])) 
)


print('Build recsys training data...')
data_titles = ['title_match', 'clevel_match', 'indus_match', 'discipline_match', 'country_match', 'region_match']
score_title = ['score']
titles = data_titles + score_title

with open(DATA_SCORE, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(titles)
    i = 0
    for key in inter_count.keys():
        i += 1
        if i % 10000 == 0:
            print('line #'+str(i)+' is being read.')
        writer.writerow(inter_count[key].features()+[inter_count[key].score()])