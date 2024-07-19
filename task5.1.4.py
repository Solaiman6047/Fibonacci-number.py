x=[]
y=[]
while x !=" ":
    x.append(int(input("Enter the x part of the coordinate:")))
    y.append(int(input("Enter the y part of the coordinate:")))
    print(x)
    print(y) 
    if x==" ":
        break
for i in range(len(x)-1):
    ans=(x[i+1]-x[i])+(y[i+1]-y[i])**0.5
print(ans)