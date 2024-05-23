##lst = []
##while True:
##    item = input("enter item: ")
##    lst.append(item)
##    ch = input("enter y to keep going enter n to quit")
##    if ch == "n":
##        print(lst)
##        break
##
##while True:
##    print("1 to append \n2 to insert\n3 to delay")
##    ch = input("enter your choice 1, 2, 3:")
##    if ch == '1':
##        item = input("enter item: ")
##        lst.append(item)
##        
##    elif ch == '2':
##        item = input("enter item: ")
##        index = input("give me an index value: ")
##        while index.isdigit() == False or 0 < int(index) > (len(lst)-1):
##            print("try again. enter something better than 0,",(len(lst)-1))
##            index = input("give me an index value: ")
##        else:
##            index=int(index)
##        lst[index] = item

##    elif ch == '3':
##
# Using a for loop, create this list below, use 'append'

cities = ["Portland", "San Francisco", "Houston", "Boston"]
states = ["Oregon", "California", "Texas", "Massachusetts" ]
citystates = []
for i in range(len(cities)):
    citystates.append(cities[i]) 
    citystates.append(states[i])

print(citystates)

days = ["monday", "wednesday", "thursday"]
days.insert(1, "tuesday")
days.append("Friday")
days.extend(["Saturday, Sunday"])
print(days)

