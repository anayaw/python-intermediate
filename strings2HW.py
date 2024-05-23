##price = float(input("give me a price of an item: "))
##otherprice = float(input("what will you pay with: "))

price = (input("give me a price of an item: "))
dot_c = price.count ('.') == 1
dot = price.find(".")
before_dot= price[0:dot-1].isdigit()
after_dot= price[dot+1:].isdigit()
##print(dot_c,before_dot, after_dot )
while dot_c == False or before_dot == False or after_dot == False:
    price = (input("give me a price of an item: "))
    dot_c = price.count ('.') == 1
    dot = price.find(".")
    before_dot= price[0:dot-1].isdigit()
    after_dot= price[dot+1:].isdigit()
##    print(dot_c,before_dot, after_dot )
else:
    price=float(price)
##    print(price,type(price))

otherprice = (input("what will you pay with: "))
dot_c = otherprice.count ('.') == 1
dot = otherprice.find(".")
before_dot= otherprice[0:dot-1].isdigit()
after_dot= otherprice[dot+1:].isdigit()
while dot_c == False or before_dot == False or after_dot == False:
    otherprice = (input("what will you pay with: "))
    dot_c = otherprice.count ('.') == 1
    dot = otherprice.find(".")
    before_dot= otherprice[0:dot-1].isdigit()
    after_dot= otherprice[dot+1:].isdigit()
else:
    otherprice=float(otherprice)
##gab = input("name : ")
##print(gab[0: :2])


##  () ()
## | -  - |
##0------- 0
## (       )
##   0 0 


 
