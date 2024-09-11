num = int(input("Enter a positive integer: "))
#using inbuilt functions
print("The binary is",bin(num).replace("0b",""))
print("The octal is",oct(num).replace("0o",""))
print("The hexadecimal is",hex(num).replace("0x",""))

#using user define functions

bin_num=num
bin_str = ''
while bin_num !=0:
    bin_str += str(bin_num % 2)
    bin_num//=2
print(f"The binary of {num} using user define function is {bin_str[::-1]}")

oct_num=num
oct_str = ''
while oct_num !=0:
    oct_str += str(oct_num % 8)
    oct_num//=8
print(f"The octal of {num} using user define function is {oct_str[::-1]}")