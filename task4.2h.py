number1=int(input("enter first number:"))
operator=input("enter operator:")
number2=int(input("enter second number:"))

if operator=="+":
    print(f"answer=",number1+number2)
elif operator=="-":
    print(f"answer=",number1-number2)
elif operator=="*":
    print(f"answer=",number1*number2)
elif operator=="/":
    print(f"answer=",number1/number2)
elif operator=="%":
    print(f"answer=",number1%number2)
else:
    print("sorry seems there is something wrong please retry")