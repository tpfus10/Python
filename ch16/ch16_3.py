#missing data 처리하기
try:
    with open('./ch16/c.csv', 'r') as f: 
        for line in f:
         print(line)
except Exception as e:
   pass


import json

# 1. json -  dump, load -> file
# 2. json -  dumps, loads -> fast API, Flask

data = {"name": "Kim", "age" : 23}
print(f"{data['name']} {type(data)} \n {json.dumps(data)} {type(json.dumps(data))}")

res_data = json.dumps(data)
print(type(json.dumps(res_data))) #보낼 때는 string
print(type(json.loads(res_data))) #받을 때는 다시 원래 형식인 dictionary