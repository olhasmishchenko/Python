speed = int(input('speed = '))
time = int(input('time = '))
if speed > 0:
    distance = speed * time
if speed < 0:
    distance = abs(speed * time)
if distance <= 100:
    print(f'Vasily ride a bike {distance} km.')
else:
    print('Max 100 km')
