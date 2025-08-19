A = int(input("Enter a positive integer: "))

sum_odd = 0
for i in range(1, A+1, 2):
    sum_odd = sum_odd + i

print("Sum of odd numbers is", sum_odd)
