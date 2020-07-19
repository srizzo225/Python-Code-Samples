#Sara Rizzo
#2020-07-19
#This program greets the user
#ask user for name
n = input("Please enter your name: ")
#these users get greeted by name
user1 = "Sara"
user2 = "Dr. Tovar"
#if Sara, greet with name
if n == user1:
    print("Hello", n)
#if Dr. Tovar, greet with name
elif n == user2:
    print("Hello", n)
#otherwise greet without name
else:
    print("Hi!")
