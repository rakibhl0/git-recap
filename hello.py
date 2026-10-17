
name = "Rako"
print("Hello ",name)


#Checke you are adult or child
def is_adult(age):
    if age >= 18:
        print("Congratulations! You are adult !!!")
    else:
        print("Hey You are child now !")

is_adult(30)

#print all even numbers from 1 to 100
for i in range(100):
    if i % 2 ==0:
        print(i)



#Login

db_user_name = "rako1"
db_password = "1234"


def login(user_name, password):
    if(db_user_nameuser_name == user_name && db_password = password):
        print("Login sucessfully")
    else:
        print("Sorry Worng  passeord!")

