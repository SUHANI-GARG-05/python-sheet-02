A = int(input("Enter a positive integer: "))

sum_even = 0
for i in range(2, A+1, 2):
    sum_even =sum_even + i

print("Sum of even numbers is", sum_even)
