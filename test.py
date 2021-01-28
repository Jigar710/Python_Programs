import pandas as pd
def dis():
    print("1. Bread : 5")
    print("2. colddrink : 15")
    print("3. cheese : 50")
    print("4. paneer : 50")
    print("5. Milk_bottle : 30")
item = ["Bread","colddrink","cheese","paneer","Milk_bottle"]
us = [0,0,0,0,0]
count = [0,0,0,0,0]
flag1 = True
while(flag1):
    username = input("Enter your name : ")
    flag2 = True
    while(flag2):
        dis()
        buy = int(input("Enter num which you want to buy : "))
        quantity = int(input("How much quantity want to buy : "))
        count[buy-1] += quantity
        us[buy-1] += 1
        f2 = input("do you want to buy other item(Y/N)? : ")
        if(f2 == "N" or f2 == "n"):
            flag2 = False
    f1 = input("Other User(Y/N)? : ")
    if(f1 == "N" or f1 == "n"):
            flag1 = False
    #print(count)
    #print(us)
data = {"items" : item, "Num_of_User" : us, "Num_of_selling_item" : quantity}
df = pd.DataFrame(data)
print(df)
    




