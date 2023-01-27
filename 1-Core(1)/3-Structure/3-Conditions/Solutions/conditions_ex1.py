# fizzbuzz q

a = int(input('Please enter a number: '))
if a%2 == 0 and a%3 == 0:
    print('fizz-buzz')
elif a%2 == 0:
    print('fizz')
elif a%3 == 0:
    print('buzz')
else:
    print(a)