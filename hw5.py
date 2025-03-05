#1.1
#pwd

#1.2
#ls

#1.3
#git pull

#1.4
#mv homework.py ~/python_decal/judy_decal

#1.5
#cat homework.py

#1.6
#nano homework.py

#1.7
#git add homework.py
#git commit -m "adding hw"
#git push origin master

#1.8
#I'm skipping this one

#1.9
#cd ~/Recent

#2.1
def datatype(x):
    output = type(x)
    return(output)

print(datatype([1, 2, 3]))

#2.2
def evenodd(y):
    if y % 2 == 0:
        return("Even")
    else:
        return("Odd")
    
print(evenodd(2))
print(evenodd(3))

#3
def sumfunc(z):
    sum1 = 0
    for i in z:
        sum1 += i
    return(sum1)

numlist = [1, 2, 3, 4, 5]
print(sumfunc(numlist))

#4.1
def dup(a):
    newlist = []
    for i in a:
        newlist.append(i)
        newlist.append(i)
    return(newlist)

list1 = ["a", "b", "c"]
print(dup(list1))

#4.2
def square(num):
    return num**2

print(square(5))
