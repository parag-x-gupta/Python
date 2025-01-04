import string as stg

# I have encrypted the messagg, I need to decrypt the message

idx_alph_dic = {}
alph_idx_dic = {}
org_method_pos = []
new_pos = []


for i in range(0,26):
    idx_alph_dic[i+1] = list(stg.ascii_lowercase)[i]
    alph_idx_dic[list(stg.ascii_lowercase)[i]] = i + 1

print(idx_alph_dic)
print(alph_idx_dic)

message = 'youtube'
shift = 6


msg_list = list(message)
for i in range(0,len(message)):
    if msg_list[i] != " ":
        position = alph_idx_dic[msg_list[i]]
        org_method_pos.append(position)
        if position <= (26 - shift):
            encrypt_index = position + shift
            new_pos.append(encrypt_index)
        else:
            encrypt_index = position + shift - 26
            new_pos.append(encrypt_index)
    else:
        new_pos.append(" ")

encrypted_message = ''
for i in range(0, len(new_pos)):
    encrypted_message += idx_alph_dic[new_pos[i]]

print(encrypted_message)

decrypted_message = ''
decrypted_letters = []

for i in range(0, len(encrypted_message)):
    # print(encrypted_message[i], alph_idx_dic[encrypted_message[i]])
    if encrypted_message[i] != " ":
        position = alph_idx_dic[encrypted_message[i]] - shift
        if position < 1:
            position += 26
            decrypted_letters.append(position)
        else:
            decrypted_letters.append(position)

for k in range(0, len(decrypted_letters)):
    decrypted_message += idx_alph_dic[decrypted_letters[k]]

print(decrypted_message)
        # alph_idx_dic[encrypted_message[i]]  - shift + 26

