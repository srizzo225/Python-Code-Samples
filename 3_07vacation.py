#Sara Rizzo
#2020-07-19
#This program calculates what day of the will you will return from a trip
#greet user and explain how days are numbered
print("Hello! I will tell you what day of the week you will be back from your trip")
print("The days are numbered 0-7, where 0 is Sunday, 1 Monday, etc.")
#ask for departure day
leave = input("Please enter departure day number:")
#ask for how many days gone
away = input("Please enter how many days you will be away:")
#convert to float
l = float(leave)
a = float(away)
#calculate and print nice message
print("You will arrive back on day", int(((l + a)) % 7))
#end program
print("Have a nice trip!")