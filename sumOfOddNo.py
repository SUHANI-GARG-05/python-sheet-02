N = int(input("Enter a positive integer: "))

sum = 0
for i in range(1, N+1, 2):
    sum = sum + i

print("Sum of odd numbers is", sum)

