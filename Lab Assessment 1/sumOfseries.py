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

print()

# loop to calculate the sum of the series
for i in range(n):
    term = int(str(series) * (i+1))  
    sum += term  

print("Sum of the series:", sum)
