num = int(input("Enter an integer: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
