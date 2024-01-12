def list_value(list,index):


    try:
        print("the element is ",list[index])
    except IndexError as e:
        raise Exception(" ind1ex is out of range",e)
                
    

limit=int(input("enter your limit:  "))
list=[]

for i in range(limit):
    number=int(input("enter your value:"))
    list.append(number)


print("list elements are:",list)
index=int(input("enter your index you want:"))







list_value(list,index)
        



