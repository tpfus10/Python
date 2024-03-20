import json

import plotly.express as px

# json load - file
# json loads - str -> dict, dict -> str

#160
mag, lat , lon = [], [], []

with open('./ch16/eq.geojson', 'r', encoding = 'utf-8') as f:
    data = json.load(f)
    print(type(data), type(data['features']), data['features'][0]) #파이썬은 타입 확인이 중요함
    for feature in data['features']:
        mag.append(feature['properties']['mag']) #eq.geojson 딕셔너리의 키가 features인 리스트 데이터의 인덱스가 0인 딕셔너리의 키가 properties인 딕셔너리의 키가 mag인 데이터
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])

fig = px.scatter_geo(lat = lat, lon = lon, size = mag)
fig.show()