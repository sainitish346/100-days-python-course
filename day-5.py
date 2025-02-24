import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_']
print("Welcome to the Password Generator: ")
nl=int(input("How many letter would you like to use in your password: "))
nn=int(input("How many numbers would you like to use in your password: "))
ns=int(input("How many symbols would you like to use in your password: "))
password=[]
for j in range(nl):
    password.append(random.choice(letters))
for j in range(ns):
    password.append(random.choice(symbols))
for j in range(nn):
    password.append(random.choice(numbers))
random.shuffle(password)
final_password=""
for i in password:
    final_password+=i
print(final_password)