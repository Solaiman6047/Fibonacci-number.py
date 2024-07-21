number1=int(input("enter first number:"))
operator=input("enter operator:")
number2=int(input("enter second number:"))

def add(number1,number2):
    return number1+number2
    
def sub(number1,number2):
    return number1-number2
    
def mult(number1,number2):
    return number1*number2
    
def div(number1,number2):
    if number2==0:
        return "undefined answer"
    else:
        return number1/number2

def mod(number1,number2):
    return number1%number2


if operator=="+":
    z=sum(number1,number2)
elif operator=="-":
    z=sub(number1,number2)
elif operator=="*":
    z=mult(number1,number2)
elif operator=="/":
    z=div(number1,number2)
elif operator=="%":
    z=mod(number1,number2)
else:
    print("undefined value")
print(z)