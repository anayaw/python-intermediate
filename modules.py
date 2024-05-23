###random choice picker code :0
##import random
##from math import floor
##print(random.choice(['eat', 'sleep', 'go to school', 'do homework', 'waste most of my time']))
##
#random numbers
##import random as r # now i can type r instead of the module name
##col = [2,3,7,8,34,6,78,0,11,6]
##print(r.choice(col))
##print(r.randrange(1,10,2)) # some random odd number from 1-10
##print(r.randrange(10)) # some random number from 0 - 10
##print(r.sample(col, 3)) # 3 random UNIQUE items from col
##print(r.choices(col, k=9)) # 9 random items from col (may repeat)

#the date
##from datetime import datetime as dt
##print(dt.now())
##print(dt.now().weekday())
##print(dt.now().date())
##print(dt.now().time())

#TURTLE WHICH I HAVEN'T DONE SINCE 8 MONTHS AGO (TODAY IS 2024-02-08)
##import turtle
##shelly = turtle.Turtle() # shelly is our turtle object
##for s in range(4):
##    shelly.forward(100) # use the same syntax as list or string methods
##    shelly.left(90)
##

#Classwork (i sleep, i should stop sleeping at 11PM..)
#numbi 1
e = ["monday", "tuesday", "wednesay", "thursday", "friday", "saturday", 'sunday']
#numbi 2
from datetime import datetime as dt
print(dt.now().weekday())
#numbi 3
import math
ses = int(input("write an integer: "))
print(math.pow(ses,2))
#numba 4,5,6
emp = ["cinna", "ava", "sameul", "jonathan", "whatever mrs shreya said", "your employee", "WHO", "where", "what", "math", "2024", "i cant think of 15 names", "da best you guys", "i will contribute to your company", "no", "yes" ]
group = int(input("how many sla-..employees do you want (under 15)?: "))
import random as r
print(r.sample(emp, group))
#it makes more sense to use the sample function because if you use choices, there is a 90% chance that it will repeat, and how are you gonna clone an employee if your broke?
#number 8
import turtle
shelly = turtle.Turtle()
for s in range(3):
    shelly.color('white smoke') 
    shelly.forward (100)
    shelly.left (144)

