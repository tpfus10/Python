import csv
from matplotlib import pyplot as plt
from pathlib import Path #개발환경에 상관없이 파일을 읽을 수 있게 함

x1, y1 = [], []
x2, y2 = [], []

#상수 정의하기 
COL_DATE = 2
COL_TMAX = 4

#데이터 출력과 읽기
with open ('./ch16/a.csv') as f: 
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line, type(line))
        x1.append(line[COL_DATE])
        y1.append(line[COL_TMAX])
        x2.append(line[2])
        y2.append(line[5])

#헤더 출력하기
for i, h in enumerate(header): 
    print(i, h)

#기온 그래프 그리기
plt.plot(x1, y1, label="TMAX")
plt.plot(x2, y2, label="TMIN")
plt.xticks(rotation = 90)
plt.legend()
plt.fill_between(x1, y1, y2, facecolor="skyblue", alpha=0.2)
plt.show()