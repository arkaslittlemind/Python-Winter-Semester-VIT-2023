onRoadprice = int(input("Enter the on road price of the bike: "))

if onRoadprice >= 200000:
    tax = 0.2 * onRoadprice
elif onRoadprice >= 100000 and onRoadprice <= 199000:
    tax = 0.15 * onRoadprice
else:
    tax = 0.1 * onRoadprice

print("The Road Tax to be levied on the bike is: Rs.", tax)