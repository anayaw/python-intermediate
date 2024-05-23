def defe(nums):
    count = 0 
    for num in nums:
        count  = count + 1
    return count
print(defe([2,2,2,2,2,2,2,2,2,2]))

def something(end,start=0, step=1):
    lst = []
    var = start
    if var<=end:
        while var <= end:
            lst.append(var)
            var += step
    else:
        while var >= end:
            lst.append(var)
            var += step
    return lst
print(something(10))
print(something(1,5,-1))
print(something(0,20,-2))

def sliceypizza(l,start=0,end=-1,step=1):
    lst=[]
    if end==-1:
        end = len(l)
    for i in range(start,end,step):
        lst.append(l[i])
    return lst
print(sliceypizza('hello',1,-1,1))
print(sliceypizza('blueberry',2,8,1))

pizzashopdowntown = 2

def prinny (food):
    global pizzashopdowntown
    yum= pizzashopdowntown + food
    return (yum)
print(prinny(3))

#var = start
#count = 0
#end = len(l)
