num = int(input("Enter a number: "))
total_digits = 0
digit_sum = 0

while num > 0:
    digit = num % 10
    total_digits += 1
    digit_sum += digit
    num //= 10

print("Total digits:", total_digits)
print("Digit sum:", digit_sum)
