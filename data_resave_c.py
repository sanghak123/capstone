import numpy as np
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


data_titles = ['title_match', 'clevel_match', 'indus_match', 'discipline_match', 'country_match', 'region_match']
score_title = ['score']
titles = data_titles + score_title

print('Parsing and building recsys training data...')
builder = InteractionCountBuilder(users, items)
select_inter_counts_and_write(INTER_COUNT_FILE, DATA_SCORE, lambda x: True, builder.build_interaction, titles)
