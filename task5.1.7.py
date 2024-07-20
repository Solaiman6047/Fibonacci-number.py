lettre=input("Enter the column's lettre: ")
number=int(input("Enter the row's number: "))
column=["a","b","c","d","e","f","g","h"]

if lettre in column and number <= 8 and number >= 1:
     let=ord(lettre)
     res=let+number
     res%=2
     if res==1:
        print("White")
     else:
        print("Black")
else:
    print("Invalid input. Please enter a valid chessboard position.")
