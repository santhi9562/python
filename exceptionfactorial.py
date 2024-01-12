try:
    num=int(input(" enter your choice:"))
    if num==0:
        print("factorial is zero")
    i=1
    
    fact=1
    while(i<=num):
        fact=fact*i
        i+=1
    print("factorial of ",num,"=", fact)
except:
    if num<0:
        raise Exception("there is no factorial in negative number")




