#Taking budget input
while True:
    try:
        budget = float(input("Enter your budget : "))
        s = budget
    except ValueError:
        print("ENTER NUMBER AS A AMOUNT")
        continue
    else:
        break

#initializing Data storage

a = {"name": [], "weight":[], "price": []}
b = list(a.values())   
name = b[0]
weight = b[1] 
price = b[2]

#Adding Product or Exiting

while True:
    try:
        choose = int(input("1.ADD\n2.EXIT\nENTER yOUR CHOISE :"))
    except ValueError:
        print("\nERROR: Choose only digits from the given option")
        continue
    else:

#Adding a product

        if choose == 1 and s>0:
            product_name = input("Enter the product name : ")
            product_weight = input("Enter the weight : ")
            product_price = float(input("Enter the price of product : "))

            #Checking Buget Constraints

        if product_price > s:
            print("you can't buy the product ")
            continue
        else:
            if product_name in name:
                ind = name.index(product_name)
                weight.remove(weight[ind])
                price.remove(price[ind])
                weight.insert(ind,product_weight)
                price.insert(ind,product_price)
                s = budget-sum(price)

                print("\n amount left",s)
            else:
                name.append(product_name)
                weight.append(product_weight)
                price.append(product_price)
                s = budget-sum(price)
                print("\n amount left", s)
                    # if budget goes zero print "NO BUDGET"
else:
    s<= 0
    print("\n NO BUDGET")





print("\n Amount left : rs.",s)
if s in price:
    print("\n Amount left can buy you a",name[price.index(s)])
print("\n\n\n GROCERY LIST")

for i in range(len(name)):
    print(name[i],weight[i],price[i])