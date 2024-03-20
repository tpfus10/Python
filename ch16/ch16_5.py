from matplotlib import pyplot as plt
import csv
import datetime as dt
from datetime import datetime

x1, y1, y2 = [], [], []

with open('./ch16/a.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader: #with 블록 내부에서 작성해야 함
        x1.append(datetime.strptime(row[2], '%Y-%m-%d'))
        y1.append(int(row[4]))
        y2.append(int(row[5]))


plt.plot(x1, y1, label = 'TMAX', color='red')
plt.plot(x1, y2, label = 'TMIN', color='blue')

plt.fill_between(x1, y1, y2, color='orange', alpha=0.2)

plt.xlabel('Date')  # x 축 레이블 추가
plt.xticks(x1, rotation= 'vertical')
plt.ylabel('Temperature')  # y 축 레이블 추가
plt.title('Temperature Trends')  # 그래프 제목 추가
plt.legend()  # 범례 추가

plt.show()  # 그래프 출력