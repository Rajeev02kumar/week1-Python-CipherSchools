age=int(input("enter your age:"))
if 0<age<=3:
    print("your ticket price is free")
elif 3<age<=10:
    print("your price ticket is 150")
elif 10<age<=60:
    print("your ticket price is 250")
else:
    print("your ticket price is 200")