dinner = {
    "starter": "samosas",
    "main course": "truffle pasta",
    "dessert": "mango sorbert",
}

for course in dinner:
    print(course, ":") # By default, the iterator variable will be a dictionaries keys.
    print(dinner[course]) # To get values, we index the dictionary with the key as before.
    print("-----")
print("*****")