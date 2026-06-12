with open("indus.txt","a") as myfile:
    mydata = myfile.write("\n Hello ")

with open("indus.txt") as myfile:
    mydata = myfile.read()
    print(mydata)