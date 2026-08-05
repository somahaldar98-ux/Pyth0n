field1 = 10
field2 = 20
field3 = 100
field4 = 200
field5 = 400
field6 = 800

total = field1 + field2 + field3 + field4 + field5 + field6
print(total)
average = total / 6
print(average)
price_per_kg = 9999
earning = total * price_per_kg
print(earning)
bag = total // 25
print (bag) 
leftover = total%25
print(leftover)
last_year = 500
print("Was it better than last year?",total>last_year)
print("Same as last year", total == last_year)
print("At least it was good",total<last_year)
