import csv

USERS_FILE        = "users.csv"
ITEMS_FILE        = "items.csv"
INTERACTIONS_FILE = "interactions.csv"

# interaction count
interaction_dict = {}
with open(INTERACTIONS_FILE, 'rb') as csvFile:
	first = True
	reader = csv.reader(csvFile, delimiter='\t')
	i = 0
	for row in reader:
		i += 1
		if first:
			first = False;
			header_interactions = row
			continue
		keyTuple = (row[0], row[1], row[2])

		if keyTuple in interaction_dict:
			interaction_dict[keyTuple] += 1
		else:
			interaction_dict[keyTuple] = 1

		if i % 500000 == 0:
			print(str(i)+' lines have been read.');

with open('interactions_count.csv', 'w') as csvFile:
	writer = csv.writer(csvFile, delimiter='\t')
	writer.writerow(header_interactions[:2]+header_interactions[3])
	for key, val in interaction_dict:
		(a, b, c) = key
		writer.writerow([a, b, c, val])
