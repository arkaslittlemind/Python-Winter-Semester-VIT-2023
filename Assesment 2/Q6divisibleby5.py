n = int(input("Enter a number: "))

last_digit = n % 10

print("The last digit is", last_digit)

if(last_digit % 5 == 0):
    print("The last digit is divisible by 5")
else:
    print("The last digit is not divisible by 5")