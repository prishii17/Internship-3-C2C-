mydic = {}
count = int(input("How many records?"))

for i in range(0, count ):
    mykey = input("Enter key:")
    mydic[mykey] = input("Enter Value:")
    
print(mydic)
