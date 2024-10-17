import random
letters = ['a','b','c','d','e']
numbers = ['1','2','3','4','5']
symbols = ['@','#','$','%','^']

print("Password Generator")

ui_letters = int(input("how many letters\n"))
ui_numbers = int(input("how many numbers\n"))
ui_symbols = int(input("how many symbols\n"))

password_list = []
for char in range(0, ui_letters):
    password_list.append(random.choice(letters))

for char in range(0, ui_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, ui_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is: {password}")