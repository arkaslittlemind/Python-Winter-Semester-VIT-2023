size = int(input("Enter the size of the triangle: "))
 
for i in range(size):
    for j in range(i+1):
        print("*", end="")
    print()