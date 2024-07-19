loanAmount=int(input("enter your laon amount:"))
age=int(input("enter your age:"))
monthlyIncome=int(input("enter your monthly income:"))
employmentStatus=input("enter your employment status(employed/unemployed):")
creditScore=int(input("enter your credit score:"))
outstandingLoan=input("enter your outstanding loan(yes/no):")
reasons=""

if age<=18:
    reasons+="Not old enough,"
if monthlyIncome<loanAmount/12:
    reasons+=" Insufficent income,"
if employmentStatus=="unemployed":
    reasons+=" Unemployed,"
if creditScore<350 or creditScore>800:
    reasons+=" Credit score out of acceptable range,"
if outstandingLoan=="yes":
    reasons+=" You have an outstanding loan"
if reasons=="":
    print("Congratulations! You are eligible for a loan")
else:
    print(f"sorry, you're not eligible for a loan Reasons:"+reasons)