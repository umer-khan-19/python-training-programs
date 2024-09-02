#1. Python program to find sum of natural numbers.
n=int(input("Enter the number to sum 1 to n: "))
sum_of_natural_number=0
if n<0:
    print("Please enter a positive number")
else:
    for i in range(1,n+1):
        sum_of_natural_number+=i
    print(sum_of_natural_number)