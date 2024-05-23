#Review
##def area_square(width):
##    return width * width
##
##def area_rectangle(width, length):
##    return width * length
##
##def area_triangle(base, height):
##    return base * height / 2
##
##def area_circle(r): # what information do you need?
##    return 3.14 * r*r# return the area of a circle
##while True:
##    ch = int(input("What input do you want? NUMBER 1-4: "))
##    if ch == 1:
##        w = float(input("enter width :"))
##        print(area_square(w))
##    elif ch == 2:
##        l = float(input("ENTER LENGTH: "))
##        w = float(input("enter width :"))
##        print(area_rectangle(w, l))
##    elif ch == 3:
##        b =float(input("ENTER BASE: "))
##        h =float(input("ENTER HEIGHT: "))
##        print(area_triangle(b, h))
##    elif ch == 4:
##        r = float(input("enter radius"))
##        print(area_circle(r))
##    else:
##        print("enter something between 1 and 4 why are you like this")


#Scopes Example
##name = "Robert Downey Jr."
##title = "The Iron Giant"
### name and title are 'global'
##def get_first_word(sentence):
##    space_index = sentence.index(' ')
##    first_word = sentence[:space_index]
### space_index, first_word, and sentence only exist here
### they are 'local' to this function!
### can you print name or title here? Try it out
##    print(name)
##    print(title)
##    return first_word
######print(sentence)
####print(space_index)
####print(first_word) # what do you think this would print? Try it out
##first_of_title = get_first_word(title)
##print(first_of_title)


#try to run the code below
##score = 0
##def check_guess(guess, answer):
##    global score
##    if guess.lower() == answer.lower():
##        score += 1 # an equals sign means you're reassigning score
##        return score
##guess1 = input("What is the fastest mammal in the world?")
##print(check_guess(guess1, "Cheetah"))
##
##guess2 = input("do cats break stuff?")
##print(check_guess(guess2, "yes"))

#Optional Parameters
##def food(name='fries', goodness = "its fine"):
##    print(name, "\t", goodness)
##food("apple")
##food(goodness="DELICOUS :D")
##food("random not tasting good food that is not good because it just doesn't taste good ")
##food("good food that tastes really good", "YUMYUMYUMYUYMYUMY")
##

#Infinite Number of Arguments!
##def max(*nums):
##    biggest_so_far = 0 # this only works for positive numbers
##    for num in nums: # nums is a collection!
##        if num > biggest_so_far:
##            biggest_so_far = num
##    return biggest_so_far
##print(max(1,2,34,7))
##print(max()) # what if we give it no arguments?

#Keyword Parameters
##def employee_info(name, position = "Labourer"):
##    print(name, "\t", position)
### you can give them in any order if you use their names!
##    employee_info(position="Supervisor", name="Kira")
##def max(*nums, positive = True):
##    if not positive:
##        return "This function only works for positive numbers!"
##    biggest_so_far = 0 # this only works for positive numbers
##    for num in nums: # nums is a collection!
##        if num > biggest_so_far:
##            biggest_so_far = num
##    return biggest_so_far
### the collections still must come first
##print(max(1,2,3,4,positive = True))
##print(max(-2,-1,-10, positive = False))










#1
#global is a variable outside of any function that is accessable in the program
#local is a variable defined inside of a function that is only accessable in the function
#2
#if you use a local variable outside of a function, you'll get a name error
#3
def minimum(nums):
    smallest = nums[0]
    for num in nums:
        if num<smallest:
            smallest=num
    return smallest
print(minimum([9,9,8, 6, 4]))

#4
def names(name, names):
    print(name, "\t", names)
names(name = "787868", names = "9090909")
##5
def you_info(name='N/A', phone='xxx-xxx-xxxx'):
    print(name, ', ', phone)
you_info("loan")
##6
def rectangle(width, length = 0):
    if length==0:
        return width * width
    elif length > 0:
        return width * length
    else:
        print("no")
print(rectangle(5, -7))
##7
def sum_or_product(*nums, yes = True):
    if yes == True:
##        product = num in nums
        count=0
        for num in nums:
            count = count + num
        return count
    elif yes == False:
        count=1
        for num in nums:
            count = count * num
        return count    
    
print(sum_or_product(4, 5, 3, 2,yes= False))
#8
#optinal parameters are useful when you have code and one is different than the other, and they both need different code
#9
#the advantage is that the argument order does not matter so you can put it in any order unless its a collection
        

    

