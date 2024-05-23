password = "sbeit"
c = 0
s = 0
d = 0
for character in password:
    if not (character.isalnum()):
        s += 1
    elif not character.isalpha() and character.isalnum():
        d += 1
    elif character.isupper():
        c += 1
if c >= 2 and d >= 2 and s >= 2:
    print("That's a strong password!")
else:
    print("You should try to make a stronger password!")


# the best way to store a name is as a string! Use quotes!
friends = ["Noah", "Marny", "Lisa", "Gurpreet", "Isaac"]
# each name is a string, separated by commas
# oops! I forgot a name! Here's one way to add another one
friends = friends + ["Jenny"] # this is list concatenation
# just like string concatenation, it makes a new list
# with all the elements from each list on the right
# in the same order they are added in
print(friends) # this will print the whole list at once
print(len(friends)) # the len function works on lists too
# a list is a collection, so we can loop through it
for name in friends: # just like we loop through strings
    print(name, "is invited to my party!")

list = ['a', 'b', 'c', 'e', 'f', 'h']
where_is_c = list.index('c') # where_is_c is the index of 'c'
number_of_sevens = list.count(7)
number_of_as = list.count('a')
where_is_h = list.index('h') # what is in where_is_h ?

vote = ["Jen", "Jayden", "Jared", "Jen", "Jen", "Jayden", "Jayden", "Jen"]
Jen_counter = 0
for  name in vote:
    if name == "Jen":
        Jen_counter +=1
print("jen vote", Jen_counter)



friends_names = ["jeremy", "jason", "jaymit", "river","lily", "jen", "ben", "harley", "frida"]
fruit = friends_names + ['lisa', 'prisha', 'nathan']



