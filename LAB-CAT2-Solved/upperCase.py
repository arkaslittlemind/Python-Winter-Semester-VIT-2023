## Function with parameter and no return value
def capitalise1(s):
    l=s.split(' ')
    ans=''
    for i in l:
        ans+=i.capitalize()+' '
    print(ans)

## Function with parameter and return value
def capitalise2(s):
    l=s.split(' ')
    ans=''
    for i in l:
        ans+=i.capitalize()+' '
    return ans


    
    
s = input("Enter a string in lower case letters: ")
capitalise1(s)
print(capitalise2(s))