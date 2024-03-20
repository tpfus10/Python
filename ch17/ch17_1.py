import requests

import plotly.express as px

import json

u = 'https://api.github.com/search/repositories?q=language:python+sort:stars'

res = requests.get(u)

data = res.json()
# print(res.json())

name = []
stargazers_count = []

for item in data['items']:
    name.append(item['name'])
    stargazers_count.append(item['stargazers_count'])

fig = px.bar(x = name, y = stargazers_count)
fig.show()

