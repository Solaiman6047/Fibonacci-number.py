number1=int(input("enter first number:"))
operator=input("enter operator:")
number2=int(input("enter second number:"))

if operator=="+":
    print(f"answer=",number1+number2)
elif operator=="-":
    print(f"answer=",number1-number2)
elif operator=="*":
    print(f"answer=",number1*number2)
elif operator=="/" and number2!=0:
    print(f"answer=",number1/number2)
elif operator=="%":
    print(f"answer=",number1%number2)
else:
    print("undefined number")