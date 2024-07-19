term=int(input("Enter the nth term of Fibonacci Sequence:"))
number1=0
number2=1
answer=0
for i in range(term):
    answer=number1+number2
    number1=number2
    number2=answer
print(number2-number1)