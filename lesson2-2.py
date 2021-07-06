math = input("please enter your math score:")
english = input("please enter your english score:")
math = int(math)
english = int(english)

if math >= 90 and english >= 90:
    print ("You have got the scholarship")
elif math < 60 or english < 60:
    print ("You will get punishment!!")

