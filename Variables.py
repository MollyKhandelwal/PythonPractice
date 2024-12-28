# named container to store anything  - variables
x=5

y=10

z=10.50

surname = "Khandelwal"

mylist = ["milk", "sugar", "wheat", 3, 10.45, True]


print(len(mylist))
# [index] -> value
# [startingIndex:EndingIndex-1] -> range of values
print(mylist[2:5])

Str=""
for x in mylist:
    print(type(x))
    Str= Str+str(x)
    # if isinstance(x, str):
    #     Str += x
    print(x)
print(Str)


for i in range(len(mylist)):
    print(i)
    print(mylist[i])
