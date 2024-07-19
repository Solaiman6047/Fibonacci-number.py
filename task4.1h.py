score=int(input("enteryour score:"))


if score<=100 and score>=90:
    print("your grade is A")
elif score<=89 and score>=80:
    print("your grade is B")
elif score<=79 and score>=70:
    print("your grade is C")
elif score<=69 and score>=60:
    print("your grade is D")
elif score<=59 and score>=0:
    print("your grade is F")
else :
    print("Invalid Degree")