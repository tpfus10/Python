cars = ['bmw', 'audi', 'subaru', 'totyota']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the reversed list:')
cars.reverse()
print(cars)

print('\nHere is the original list:')
cars.reverse()
print(cars)

print(len(cars))

