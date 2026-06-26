print('Hello, this is a greeting program')
name = input('Firstly, please tell us your name ').strip().capitalize()
try:
    age = int(input('Tell us your age '))
except ValueError:
    print('Please enter a valid number for your age')
    exit()

print(f'Thank you, {name}, now I know that you are {age} years old. Next year you will be {age + 1} years old')
