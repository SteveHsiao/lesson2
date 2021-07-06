math = input("please enter your math score:")
english = input("please enter your english score:")
math = int(math)
english = int(english)

if math >= 90 and english >= 90:
    print ("You have got the scholarship")
elif math == 100 or english == 100:
    print ("You have got the scholarship")
else:
    print ("You didnt got any scholarship")
