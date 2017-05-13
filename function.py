#var integer

a=1

def change_integer(a):
    a=a+1
    return a

print change_integer(a)
print a

#list

b=[1,2,3]

def change_list(b):
    b[0]=b[0]+1
    return b

print change_list(b)
print (b)

#leap_year test
def leap_year(a,b,c):
    if a % 400 == 0:
        if a % 100 == 0:
            if a % 4 == 0:
                print (True)
            else:
                print (False)
        else:
            print(True)
    else:
        print (False)
        # different 
def leap_year(a,b,c):
     if a % 400 == 0:
             print (True)
     elif a % 100 == 0:
             print(False)
     elif a % 4 == 0:
             print (True)
