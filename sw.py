f = open('c.txt','a') 
name = input("what is your name kid?")
a = "GUESS WHAT!  CHECK THE FILE,"+name 
f.write(a)
f.write('\n')
f.close()
