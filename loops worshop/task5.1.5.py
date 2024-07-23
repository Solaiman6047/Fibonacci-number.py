letters="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
letters_cap="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
text=input("Enter text: ")
n=int(input("Enter the shift amount: "))
result=""
if n>=26:
    print("Error:the shift amount must be less than 26")
else:
    for i in range(len(text)):
        for j in range(len(letters)):
            if text[i] == letters[j]:
                result+=letters[j+n]
                break
            elif text[i] == letters_cap[j]:
                result+=letters_cap[j+n]
                break
        else:
            result+=text[i]
print(result)