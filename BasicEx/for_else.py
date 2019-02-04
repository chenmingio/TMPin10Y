while 1:

    for n in range(2, 10):
        if n < 5:
            print("{} < 5".format(n))
            break
    else:
        print("in else")
