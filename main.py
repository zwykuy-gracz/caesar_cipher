import string

letters = string.ascii_lowercase
letters += ' '
letters_list = (list(letters))
digit_list = []
for i in range(27):
    digit_list.append(i)
letters_index_dict = dict(zip(letters_list, digit_list))

user_input_message = input("tell me your message: ")
user_input_list = list(user_input_message)
user_input_indeces = []

for i in range(len(user_input_list)):
    user_input_indeces.append(letters_index_dict[user_input_list[i]])

# print(user_input_indeces)  

def encrypting_message(user_input_indeces):
    movement = int(input('Tell me how many places to move the coding? '))
    for i in range(len(user_input_indeces)):
        user_input_indeces[i] = user_input_indeces[i] + movement
        if user_input_indeces[i] > 27:
            user_input_indeces[i] -= 27
    return user_input_indeces

def decrypting_message(user_input_indeces):
    movement = int(input('Tell me how many places to move the coding? '))
    for i in range(len(user_input_indeces)):
        user_input_indeces[i] = user_input_indeces[i] - movement
        if user_input_indeces[i] < 0:
            user_input_indeces[i] += 27
    return user_input_indeces

def printing_message_after_operation(moved_indeces):
    final_output = ''
    for i in range(len(moved_indeces)):
        keys = [k for k, v in letters_index_dict.items() if v == moved_indeces[i]]
        final_output += keys[0]
    print(final_output)


users_option_enc_dec = input("you want to [E]ncrypt or [D]ecrypt a message? ").lower()

if users_option_enc_dec == 'e':
    moved_indeces(user_input_indeces)
    printing_message_after_operation(moved_indeces)