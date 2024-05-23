food={'coffee':2, 'bagel':3, 'donut':1, 'sandwich' :5}

empty={}

sports={}
sports['soccer']=7
sports['rugby']=9
sports['basketball']=11
print(sports)

user={'brianfurry':9018293, 'jennyalsofurry':119238}
user['duck']=178375
user['uh..']=92537
print(user)


movies= {"Best Picture": "Mickey Mouse", "Best Actor": "Mickey", "Best Actress": "Minnie", "Animated Feature": "Mouse"}
movies['supporting']='anyone'
movies['Best Picture']="FROZEN??"
print(movies)


fruits = {'apple': 6, 'strawberry': 7, 'watermelon': 3, 'pineapple': 4}
fruits['orange']=17
fruits['watermelon']=5
print(fruits)

something={}
while True:
    key=input("enter a word: ")
    value=float(input("enter a value: "))
    something[key]=value
    print(something)
    ch=input("do you want to keep going? y=yes n = no: ")
    if ch == 'n':
        print('okk byee')
        break
    else:
        print('go on')
        
