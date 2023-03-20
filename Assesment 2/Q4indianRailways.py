gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))

base_fare = float(input("Enter the base fare: "))

if ((gender == "M" or gender == "m") and age >= 60):
    concession = 0.4 * base_fare
    fare = base_fare - concession
    print("Eligible for senior citizen concession")
    print("Ticket amount:", fare)

elif ((gender == "F" or gender == "f") and age >= 58):
    concession = 0.5 * base_fare
    fare = base_fare - concession
    print("Eligible for senior citizen concession")
    print("Ticket amount:", fare)

else:
    print("Not eligible for senior citizen concession")
    print("Ticket amount:", base_fare)