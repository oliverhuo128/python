# copy your solution to the Exercise into this file, below: 

user_string = input('please enter a string to append to file')
f = open('log_file.txt', 'a')
f.write(user_string + '\n')
f.close()

f = open('log_file.txt', 'r')
lines = f.readlines()
f.close()
print(*lines, sep='\n')