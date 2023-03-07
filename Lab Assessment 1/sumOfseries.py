

n =int(input("Enter number of terms in series: "))
series = int(input("Enter starting value of the series: ")) 
sum = 0  

#loop to print the series
start = series
sum1 = 0;
for i in range(0, n):
    print(start, end = " ")
    sum1 += start
    start = (start * 10) + series

print("\n")

# loop to calculate the sum of the series
for i in range(n):
    term = int(str(series) * (i+1))  # calculate the i-th term of the series
    sum += term  # add the i-th term to the sum variable

print("Sum of the series:", sum)
