while True:
    num = int(input("Please enter a number: "))

    if num>10:
        print("Number is greater...")
    elif num<0:
        print("Number is smaller...")
    else:
        print("Number within 1 and 10: ", num)
        break