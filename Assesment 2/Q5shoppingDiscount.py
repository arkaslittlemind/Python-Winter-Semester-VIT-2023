bill_amount = float(input("Enter the bill amount: "))
item_category = input("Enter the item category: ")

discount = 0

if item_category == "Saree":
    discount = 0.2

elif (item_category == "Ethnic Wears" or item_category == "Gents Wears" or item_category == "Kids Wears"):
    discount = 0.15

net_bill_amount = bill_amount - (discount * bill_amount)

if net_bill_amount > 6000:
    net_discount = 0.05 * net_bill_amount

net_bill_amount = net_bill_amount - net_discount

print("Net bill amount:", net_bill_amount)