year = int(input('Please give me year: '))
if year % 4 == 0 or (year % 400 == 0 and year % 100 > 0):
    print('Leep year')
else:
    print("No Leep year")
