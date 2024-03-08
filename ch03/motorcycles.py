mortorcycles = ['honda', 'yamaha', 'suzuki']
print(mortorcycles)
mortorcycles[0]='ducati'
print(mortorcycles)
mortorcycles[-1]='kia'
print(mortorcycles)

mortorcycles.append('hyundai')
print(mortorcycles)

mortorcycles.insert(1,'tesla') 
print(mortorcycles)

del mortorcycles[0]
print(mortorcycles)

popped_motocycle = mortorcycles.pop()
print(mortorcycles) 
print(f'The last mortorcycle I owned was a {popped_motocycle}.')

first_owned = mortorcycles.pop(0)
print(mortorcycles) 
print(f'The first mortorcycle I owned was a {first_owned}.')

too_ugly = 'kia'
mortorcycles.remove(too_ugly)
print(mortorcycles)

mortorcycles2 = ['honda', 'tesla', 'yamaha', 'hyundai', 'tesla']
mortorcycles2.remove('tesla')
print(mortorcycles2)

