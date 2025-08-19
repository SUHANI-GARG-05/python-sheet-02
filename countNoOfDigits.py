n = int(input("Enter a number: "))

if n == 0:
    count = 1
else:
    count = 0
    num = abs(n)  
    while num > 0:
        num //= 10  
        count += 1

print("Number of digits:", count)
