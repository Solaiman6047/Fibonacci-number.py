list=[7,3,0,1]
ans=''

for i in range(len(list) - 1):
    if list[i]<list[i+1]:
        ans="True"
    else:
        ans="False"
        break
print(ans)                                  #Workshop1