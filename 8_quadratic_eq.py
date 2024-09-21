a,b = map(float, input("Enter value of a and b for calculation (a + b)^2 and (a - b)^2 : " ).split())
result1 = a**2 + 2*a*b + b**2
result2 = a**2 - 2*a*b + b**2
print(f'The result of (a + b)^2 is {result1} \n The result of (a - b)^2 is {result2}')