x=[]
y=[]
ans=0

while True:
    x_input=input("Enter the x part of the coordinate:")
    if x_input==" ":
        break
    x.append(int(x_input))
    y_input=input("Enter the y part of the coordinate:")
    y.append(int(y_input))
    
if len(x)<2:
    print("Error: Not a polygon.")
    
else:
    for i in range(len(x)):
        ans+=((x[i-1]-x[i])**2+(y[i-1]-y[i])**2)**0.5
    print(f"Perimeter= {ans}")