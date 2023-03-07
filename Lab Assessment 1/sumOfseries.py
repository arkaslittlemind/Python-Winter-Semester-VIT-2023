n = int(input("Enter number of terms: "))
s = int(input("Enter number: "))

start = s
sum = 0
for i in range(0, n):
    print(start, end =" ")
    sum += start
    start = (start * 10) + s
    