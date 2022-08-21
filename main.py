import string

letters = string.ascii_lowercase
letters_list = (list(letters))
digit_list = []
for i in range(26):
    digit_list.append(i)

# print(digit_list)

letters_index_dict = dict(zip(letters_list, digit_list))
# print(letters_index_dict.items())
user_input = input("tell me your message: ")
user_input_list = list(user_input)
user_input_indeces = []

for i in range(len(user_input_list)):
    user_input_indeces.append(letters_index_dict[user_input_list[i]])

print(user_input_indeces)  

def encrypting(user_input_indeces):
    movement = int(input('Tell me how many places to move the coding? '))
    for i in range(len(user_input_indeces)):
        # value_of_index_i = user_input_indeces[i]
        user_input_indeces[i] = user_input_indeces[i] + movement
        if user_input_indeces[i] > 26:
            user_input_indeces[i] -= 26
    return user_input_indeces

moved_indeces = encrypting(user_input_indeces)
print(moved_indeces)