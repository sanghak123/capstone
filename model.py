'''
Modeling users, interactions and items from
the recsys challenge 2017.

by Daniel Kohlsdorf
'''

class User:

    def __init__(self, title, clevel, indus, disc, country, region):
        self.title   = title
        self.clevel  = clevel
        self.indus   = indus
        self.disc    = disc
        self.country = country
        self.region  = region

class Item:

    def __init__(self, title, clevel, indus, disc, country, region):
        self.title   = title
        self.clevel  = clevel
        self.indus   = indus
        self.disc    = disc
        self.country = country
        self.region  = region

class Interaction:
    
    def __init__(self, user, item, interaction_type):
        self.user = user
        self.item = item
        self.interaction_type = interaction_type

    def title_match(self):
        return float(len(set(self.user.title).intersection(set(self.item.title))))

    def clevel_match(self):
        if self.user.clevel == self.item.clevel:
            return 1.0
        else:
            return 0.0

    def indus_match(self):
        if self.user.indus == self.item.indus:
            return 1.0
        else:
            return 0.0

    def discipline_match(self):
        if self.user.disc == self.item.disc:
            return 2.0
        else:
            return 0.0

    def country_match(self):
        if self.user.country == self.item.country:
            return 1.0
        else:
            return 0.0

    def region_match(self):
        if self.user.region == self.item.region:
            return 1.0
        else:
            return 0.0

    def features(self):
        return [
            self.title_match(), self.clevel_match(), self.indus_match(), 
            self.discipline_match(), self.country_match(), self.region_match()
        ]

    def label(self): 
        if self.interaction_type == 4: 
            return 0.0
        else:
            return 1.0


class InteractionCount:
    
    def __init__(self, user, item, i0, i1, i2, i3, i4, i5):
        self.user = user
        self.item = item
        self.i0 = i0
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.i4 = i4
        self.i5 = i5

    def title_match(self):
        return float(len(set(self.user.title).intersection(set(self.item.title))))

    def clevel_match(self):
        if self.user.clevel == self.item.clevel:
            return 1.0
        else:
            return 0.0

    def indus_match(self):
        if self.user.indus == self.item.indus:
            return 1.0
        else:
            return 0.0

    def discipline_match(self):
        if self.user.disc == self.item.disc:
            return 2.0
        else:
            return 0.0

    def country_match(self):
        if self.user.country == self.item.country:
            return 1.0
        else:
            return 0.0

    def region_match(self):
        if self.user.region == self.item.region:
            return 1.0
        else:
            return 0.0

    def features(self):
        return [
            self.title_match(), self.clevel_match(), self.indus_match(), 
            self.discipline_match(), self.country_match(), self.region_match()
        ]

    def score(self): 
        if self.i4 != 0:
            return -10.0
        return self.i1+self.i2*5.0+self.i3*5.0+self.i5*20.0

