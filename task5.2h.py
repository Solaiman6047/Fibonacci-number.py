end_number=int(input("print prime numbers till the number:"))
answer=[]

for i in range(2,end_number+1):
    for j in range(2,(i//2)+1):
        if i%j==0:
            break
    else:
        answer.append(i)
print(answer)