try:
    number=input("enter the value:    ")
except KeyboardInterrupt as e:
    raise Exception("invalid")