import csv
from collections import defaultdict


f =  open('customerdata.csv')
reader = csv.DictReader(f)

data = []

for row in reader:
    data.append(row)

states_dict = {}
states_list = []

d = defaultdict(list)

for row in data:
    # row["Spent Past 30 Days"] = re.sub(r'[^\d.]', '', row["Spent Past 30 Days"])
    # if float(row["Spent Past 30 Days"]) > 0:
    # print(row["State"], row["Favorite Radio Station"])
    # states_list.append(row['State'], row['Favorite Radio Station'])
    states_list.append(d[row['State']].append(row['Favorite Radio Station']))
print(sorted(states_list))