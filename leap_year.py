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