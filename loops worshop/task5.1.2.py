my_list=[0,1]
n=int(input("enter the number"))
if len(my_list)>=4:
    for i in range(len(my_list) - 1):
        if my_list[i]>my_list[i+1]:
         print("list not sorted")
         break
    else:
        print(my_list[n:-n])
else:
    print("list too short")