#To find square root of a number we ahve many ways.

num = int(input("Enter a number: "))
print(f'The square root of {num} is {num**0.5}')
#In above line of code we use exponend of a number with 0.5, it give result for  negative number in complex number.

import math
print(f'The square root of {num} is {math.sqrt(num)}')
#In above code of line we use inbuilt function but if we give it negative number it gives valueError.

print(f'The square root of {num} is {pow(num,0.5)}')
#In above line of code we use pow() inbuilt function it can handle negative number and give result in comlex number.

