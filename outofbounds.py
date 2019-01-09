""" my_list = list("Hello")

for i in range(len(my_list)):
    try:
        if i > 0:
            print(my_list[i-1])
        print("Sup")
    except:
        pass
    
    try:
        print(my_list)
    except:
        pass """

i = 0
j = 1
both = (i,j)
print(both)
print(type(both))