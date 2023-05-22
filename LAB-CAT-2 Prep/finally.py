def func1():
    
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    
    except IndexError:
        print("Index out of range")
        return 0
    
    ##finally:
        ##print("Finally block is always executed")
    
    print("End of program")
        
x = func1()
print(x)