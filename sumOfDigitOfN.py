num = int(input("Enter an integer: "))
sum  = 0

while (num > 0):
    digit = num % 10     
    sum = sum + digit   
    num = num // 10            

print("Sum of digits = ", sum)
