num1, num2 = map(int,input("Enter two number: ").split())

"""
#with third variable
print(f'Before swaping numbers {num1} {num2}')
temp = num1
num1 = num2
num2 = temp
print(f'after swaping numbers {num1} {num2}')
"""

"""
#without third variable using + - operators
print(f'Before swaping numbers {num1} {num2}')
num1 +=num2
num2 = num1-num2
num1 -= num2
print(f'after swaping numbers {num1} {num2}')
"""

"""
#without third variable using // * operators
print(f'Before swaping numbers {num1} {num2}')
num1 *= num2
num2 = num1//num2
num1 //=num2
print(f'after swaping numbers {num1} {num2}')
"""


#without third variable using xor '^' operators
print(f'Before swaping numbers {num1} {num2}')
num1 ^= num2
num2 = num1^num2
num1 ^=num2
print(f'after swaping numbers {num1} {num2}')
