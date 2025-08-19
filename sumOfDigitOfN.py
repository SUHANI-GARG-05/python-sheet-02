
N = int(input("Enter an integer: "))

sum_digits = 0
num = abs(N)

while num > 0:
    digit = num % 10     
    sum_digits += digit   
    num //= 10            

print("Sum of digits of", N, "is", sum_digits)
