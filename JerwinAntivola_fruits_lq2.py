prices = {"Mango": 4,"Banana": 2,"Aratiles": 1.5,"Macopa": 3,}
stock = {"Mango": 10,"Banana": 2,"Aratiles": 50,"Macopa": 15,}
for i in prices:
    print(i)
    print ("price : %s" % prices[i])
    print ("stock : %s" % stock[i])
    print ("\n")

total = 0
for key in prices:
    print (prices[key] * stock[key])
    total = total + prices[key] * stock[key]

print ("\n")
print ("total expected income")
print (total)
