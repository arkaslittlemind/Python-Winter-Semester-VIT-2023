try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    
except IndexError:
    print("Index out of range")
    
finally:
    print("Finally block is always executed")