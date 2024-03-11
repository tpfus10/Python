#dump와 dumps/load와 loads

#json
import json

data = '{"name" : "Kim", "age" : 23}' #string
member = {"name" : "Lee", "age" : 24} #dictionary

with open('member2.json', 'w') as w_file:
    json.dump(member, w_file)

with open('member2.json', 'r') as r_file:
    d = json.load(r_file)
    print(d, type(d))

#가장 많이 쓰는 형태
d2 = json.dumps(member)
print(d2, type(d2))

d3 = json.loads(d2)
print(d3, type(d3), d3["name"])

#pickle
import pickle

data = [1, 2, 3, 4, 5]
with open('dump_member.pk', 'wb') as w_file:
    pickle.dump(data, w_file)

#가장 많이 쓰는 형태
with open('dump_member.pk', 'rb') as r_file:
    d5 = pickle.load('dump_member.pk')
    print(d5)


