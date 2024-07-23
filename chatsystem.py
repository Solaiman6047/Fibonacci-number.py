def register_user():
    x=input("register user:")
    return x
user1=register_user()
user2=register_user()
def sending_mess():
    print(f'{user1}:Type "s" to send a message(if no write "d"):')
    x=input()
    if x =="s":
        print(f"message from {user1} to {user2}:")
        message=input()
        print(f'{user2}:You received a message')
        return message
    elif x=="d":
        print(f'{user2}:Type "s" to send a message(if no write "d"):')
        y=input()
        if y =="s":
            print(f"message from {user2} to {user1}:")
            message=input()
            print(f'{user1}:You received a message')
            return message
        elif y=="d":
            print("")
    else:
        print("please try again")
message=sending_mess()
chat={
    user1:[],
    user2:[]
}
chat.update({user1:message})
chat.update({user2:message})