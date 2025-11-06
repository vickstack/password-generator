import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


user_letters = int(input("How many letters would you like in your password?\n"))
user_numbers = int(input("How many numbers would you like in your password?\n"))
user_symbols = int(input("How many symbols would you like in your password?\n"))


for letter in letters:
    random_letters = random.choices(letters, k=user_letters)

for number in range(1,11):
    random_numbers = random.choices(numbers, k=user_letters)

for symbol in symbols:
    random_symbols = random.choices(symbols, k=user_symbols)
    
merge_inputs = random_letters + random_numbers + random_symbols

#combined_inputs1 = random.choices(merge_inputs, k = user_letters + user_numbers + user_symbols)

print("Here is your password: " + ''.join(merge_inputs))


