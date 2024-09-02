#3. Python program to find numbers divisible by another number.
"""
for this problem we make a function called find_divisible_numbers and it takes three parameters(start,end,dividor)
"""
def find_divisble_number(start,end,divisor):
    result =[]
    for num in range(start,end+1):
        if num%divisor==0:
            result.append(num)
    return result

start,end,divisor = input("Enter numbers start, end and divisor: ").split()

print(f"Numbers between {start} to {end} is divisible by {divisor} is {find_divisble_number(int(start),int(end),int(divisor))}")
