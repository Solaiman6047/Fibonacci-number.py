contacts={
    "Hana":"01227523536",
    "Menna":"0100946884",
    "Mohamed":"0458292316"
}
favorite_contact={
    "Mom":"01227523536"
}
def add(name,number):
    if name in contacts:
        print("contact already there")
    else:
        contacts.update({name:number})
    print(contacts)
    
def delete_contact(name):
    del contacts[name]
    print(contacts)
    
def search_contact(name):
    if name in contacts:
        print(contacts.get(name))
    else:
        print("Contact not found")
    
def view():
    print(contacts)

def add_to_fav(name,number):
    favorite_contact.update({name:number})
    print(favorite_contact)

def update_contact(name,number,new_number):
    if name not in contacts:
        print("No contact found")
    else:
        contacts.update({name:number,name:new_number})
        print(contacts)
    
def get_name():
    name=input("Enter name: ")
    return name
def get_number():
    number=input("Enter number: ")
    return number
    
print("Enter feature(add/delete/search/view/add to fav/update): ")
x=input()
if x=="add":
    name=get_name()
    number=get_number()
    add(name,number)
elif x =="delete":
    name=get_name()
    delete_contact(name)
elif x=="search":
    name=get_name()
    search_contact(name)
elif x=="view":
    view()
elif x =="add to fav":
    name=get_name()
    number=get_number()
    add_to_fav(name,number)
elif x=="update":
    name=get_name()
    number=input("Enter old number: ")
    new_number=input("Enter new number: ")
    update_contact(name,number,new_number)
else:
    print("Unvalid feature")