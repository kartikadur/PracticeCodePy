#Version 1.0 - 70 char
for x in range(1, 101):print("Fizz"*(not(x%3))+"Buzz"*(not(x%5))or x)

#Version 2.0 - 63 char
for x in range(1,101):print("Fizz"[x%3*4:]+"Buzz"[x%5*4:]or x)