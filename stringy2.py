code = "eg!srtohrsmecvpbixndexg avgrentvioxrsstiesmy mzakh leeukrja'vyuaoovdYc"
print(code[-2::-3])

s ="missisagua"
print(s.count('s'))

print(s.find('s'))

j = '123hi'
print(j.isalnum())


a = "boop".count("o") # a is 2 because there are 2 o's in boop
b = "title".find("t") # b is 0 because the first t is at index 0
c = "StR1nG".isalnum()
# c is True because the string is only letters and numbers
d = "Hello World!".isalpha()
# d is False because there is a space and !
e = "1234".isdigit()
# e is True because our string is all numbers
f = "HAYDEN".isupper()
# f is True because all the letters are uppercase
g = "hayden123".islower()
# g is True because all the letters are lowercase
h = "banana".replace('a', 'u')
#1
#a method is sort of like a function but for a certain type of object, in this case, string
#2
##isleep = input("what ur name")
##print(isleep[0].upper()+isleep[1:]) 
#3
##y = input("name pls: ")
##print(y.title())
#4
num = input("whats ur fav number: ")
while num.isdigit() == False:
    num = input("whats ur fav number: ")
if num.isdigit() == True:
    num = int(num)
    print("ur fav number is...", num, type(num))
 #5
one = input("ONE digit: ")


while one.isdigit() == False:
    one = input("ONE digit: ")
if one.isdigit() == True:
    one = int(one)
    print(one, type(one))
two = input("enter le digit :l< : ")
while two.isdigit() == False:
    two = input("enter le digit:|< : ")
if two.isdigit() == True:
    two = int(two)
    print(two, type(two))
three = one + two       
print(three)
#7
ok = "mow mow mow your boat"
print(ok.replace('m', 'r'))
