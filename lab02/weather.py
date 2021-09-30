x = input('Please enter the highest value: ')
y = input('please enter the lowest value: ')
num1 = int(x)
num2 = int(y)
print(num1, '-', num2, '=', num1-num2)
orders = [62, 62, 60, 58, 60, 63, 64, 65, 68, 67]
average = sum(orders) / len(orders)
print("The average temperature at noon is " + str(round(average, 2)) + "˚F")
temp = input("type in the temperature in Fehrenheit: ")
Celsius1 = (int(temp) - 32)*5/9
Celsius2 = round(Celsius1, 1)
print("Temperature", temp, "˚F =", Celsius2, "˚C")
