# with open('./pythonplus/name.txt') as file:
#     for line in file:
#     for line in file.readlines():
#         print(line.rstrip()) #오른쪽에 붙은 걸 떼는 작업

# print('A', end = ' ')
# print('B', end = ' ')

# import csv
# with open('./pythonplus/name2.csv') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     for row in reader:
#         print(row) #오른쪽에 붙은 걸 떼는 작업

#C:|/dev/aaa/a.txt -> 리눅스
#/c:\dev\aaa\a.txt -> 윈도우
#=>path를 써주면 신경쓰지 않아도 됨

import os 
from pathlib import Path

#dir과 file의 path
file_path = Path('./pythonplus/name.txt')
dir_path = Path('./pythonplus') #pathlib 모듈의 Path 클래스를 임포트

print(file_path)
print(dir_path)

#디렉토리의 파일 모두 출력하기
for s in os.listdir():
    print(s)  

for d in os.listdir():
    print(d, os.path.isdir(d))

no_file = Path('./pythonplus/b.txt')
print(os.path.exists(no_file))

#경로 쪼개기
print(os.path.split(Path('./pythonplus/name.txt')))
print(Path('pythonplus', 'name.txt'))

#파일에 저장하기
with open(file_path, 'a') as file: # w는 덮어쓰기, a는 추가하기
    file.write('aaa\n')
    file.write('aaa\n')
    file.write('aaa\n')

#파일 예외처리하기1
none_path = Path('./pythonplus/name3.txt')
if none_path.exists():
    with open(none_path) as file:
        for line in file:
            print(line)

#파일 예외처리하기2
try:
    with open(none_path) as file:
        for line in file:
            print(line)

except Exception as e:
    pass

#json
import json
#import pickle

contents = json.dumps(['4', '5', '6', '7'])
file_path.write_text(contents)


# data = json()
# type(data)

# data = json.parse("{'a': 1, 'b' : 2}")
# type(data)
# print(data.a)
# print(data.b)