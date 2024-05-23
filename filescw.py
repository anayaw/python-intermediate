##mystery_dict = {}
##my_keys = []
##my_values = []
##def key_fetcher(*keys):
##    for key in keys:
##        my_keys.append(key)
##def value_fetcher(*vals):
##    for val in vals:
##        my_values.append(val)
##def dict_creator(key_list, val_list, dict = mystery_dict):
##    for i in range(len(key_list)):
##        dict[key_list[i]] = val_list[i]
##    return dict
##key_fetcher(1,2,3,4)
##value_fetcher('one', 'two', 'three', 'four')
##new_dict = dict_creator(my_keys, my_values)
##print(new_dict)

##file = open("C:\\Users\\ucbra\\OneDrive\\Documents\\Desktop\\UC Academy\\Anaya\\Python Intermidiate\\candy_text.txt",'r')
##fileo = file.read()
##print(fileo)
##
##file = open("C:\\Users\\ucbra\\Downloads\\long_poem.txt", "r")
##fielle = file.readlines()
##print(fielle)
##
##file = open("C:\\Users\\ucbra\\Downloads\\long_poem.txt", "r")
##fielle = file.readlines()
##print(fielle)
##file= open("C://Users//ucbra//OneDrive//Documents//Desktop//UC Academy//Anaya//Python Intermidiate//story.txt")
##title = file.readline()
##print(title.upper())
##for line in file:
##    print (line.strip())
##x = file.read()
##file.close()
##
##
##with open('best_food_24.txt', 'a') as f:
##    f.write('friesss')
##    f.write("wtv you likee")
##
##f = open('your_name.txt','w')
##name = input("what is your name kid?")
##f.write("GUESS WHAT!  CHECK THE FILE,"+name )
##f.close()

#1
##file= open("C://Users//ucbra//OneDrive//Documents//Desktop//UC Academy//Anaya//Python Intermidiate//candy_txt.txt")
####i = file.read()
####print(i)
##
##candy =[]
##for line in file:
##    candyname,price = line.split(',')
##    candy.append(candyname)
##print(candy)
##
##file = open("C://Users//ucbra//OneDrive//Documents//Desktop//UC Academy//Anaya//Python Intermidiate//long_poem.txt", "r")
##fill = file.readlines()
##print(fill)
##
##
##f = open("C://Users//ucbra//OneDrive//Documents//Desktop//UC Academy//Anaya//Python Intermidiate//fileknow.txt",'w')

##f.write("file object is a file object",)
with open(".txt", 'w') as f:
    for i in range(10, 0, -1):
        b="*"*i
        print(b)
        f.write(b)
        f.write('\n')
f.close()