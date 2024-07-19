total=int(input("enter your total purchase amount:"))
years=int(input("enter how many years have you been a member of the bookstore:"))
complaints=int(input("enter number of complains you've filled past year:"))
purchases=int(input("enter number of purchases you've made past year:"))
discount=total

complaints*=2


if years>10:
    discount*=(1+(10/100)-(complaints/100))
    if discount<0:
        discount=0
elif years<=10 or years<=6:
     discount*=(8/100)-(complaints/100)
     if discount<0:
         discount=0
else:
     discount*=(1+(5/100)-(complaints/100))
     if discount<0:
         discount=0
         
 
         
if purchases>20:
    if discount==0:
        discount=total
    discount*=(5/100)
    
print(f"Net discount amount=$",discount)
print(f"new total purchase amount=$",total-discount)