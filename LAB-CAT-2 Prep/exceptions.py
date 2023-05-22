##a = input("Enter a number: ")
##print(f"Multiplication table of {a} is: ")

##try:
    ##for i in range(1, 11):
        ##print(f"{int(a)} x {i} = {int(a) * i}") 

##except ValueError:
    ##print("Cant multiply string with int")
    
##print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
    
except ValueError:
    print("You must enter an integer")
    

except IndexError:
    print("Index out of range")
    a = [6, 3]