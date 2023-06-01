print("Enter the comma separated 4 digit binary number sequence: ")
items = []

nums = [x for x in input(). split(',')]

for p in nums:
    x= int(p, 2)
    if not x % 5:
        items.append(p)

print(',' . join(items))

