# Copy below your solution from "Concept Check: Birthday Greeting"

first_name = input("Please enter your first name: " )
second_name = input("Please enter your second name: ")
age = int(input("Please enter your age:"))

bday_msg = "Greetings, {} {}! On your next birthday you will be {}.".format(first_name.title(), second_name.title(), age+1)
print(bday_msg)