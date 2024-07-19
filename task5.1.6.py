print("Enter *d* to converts a decimal number to its binary equivalent and *b* to converts a binary number to its decimal equivalent")
what_to_do=input("d/b: ")
result=""

if what_to_do=="d":
    n=int(input("Enter the decimal number: "))
    if n==0:
        print("The binary equivalent is: 0")
    else:
        while n > 0:
            result += str(n % 2)
            n //= 2
        print(f"The binary equivalent is: {result}")
elif what_to_do == 'b':
    n = input("Enter the binary number: ")
    result = 0
    
    for digit in n:
        result = result * 2 + int(digit)
    
    print(f"The decimal equivalent is: {result}")
else:
    print("Invalid input. Please enter 'd' or 'b'.")