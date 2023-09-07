age = int(input("Enter age -> "))
mylist = [1,6,7,8, 20, 49, 11, 15, 39, 78, 55, 41, 39]

for value in mylist:
    diff = value - age
    if diff < 0:
        diff *= -1
        print(f"You are {diff} years older than {value}")
        
    else:
        print(f"You are {diff} years younger than {value}")

        