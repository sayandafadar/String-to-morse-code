morse_codes = {
    'a': '*-',
    'b': '-***',
    'c': '-*-*',
    'd': '-**',
    'e': '*',
    'f': '**-*',
    'g': '--*',
    'h': '****',
    'i': '**',
    'j': '*---',
    'k': '-*-',
    'l': '*-**',
    'm': '--',
    'n': '-*',
    'o': '---',
    'p': '*--*',
    'q': '--*-',
    'r': '*-*',
    's': '***',
    't': '-',
    'u': '**-',
    'v': '***-',
    'w': '*--',
    'x': '-**-',
    'y': '-*--',
    'z': '--**',
    ' ': '/'

}

# letter_codes = {
#      '*-': 'a',
#      '-***': 'b',
#      '-*-*': 'c',
#      '-**': 'd',
#      '*': 'e',
#      '**-*': 'f',
#      '--*': 'g',
#      '****': 'h',
#      '**': 'i',
#      '*---': 'j',
#      '-*-': 'k',
#      '*-**': 'l',
#      '--': 'm',
#      '-*': 'n',
#      '---': 'o',
#      '*--*': 'p',
#      '--*-': 'q',
#      '*-*': 'r',
#      '***': 's',
#      '-': 't',
#      '**-': 'u',
#      '***-': 'v',
#      '*--': 'w',
#      '-**-': 'x',
#      '-*--': 'y',
#      '--**': 'z',
#      '/': ' '
# }




# keys = list(morse_codes.keys())
# vals = list(morse_codes.values())

# print(keys[vals.index('*--')])


morse_list = []

morse_string = ''
# reverse_string = ''

# choose_what = input('What do you want to convert?\nType "to_code" to convert to morse code,\nor type "to_letter" to '
#                     'convert to actual letter.\n ')
# #
# if choose_what == "to_code":
user_input = input('Enter a word: ').lower()
for word in range(len(user_input)):
    letter = user_input[word]
    code_word = morse_codes[letter]
    morse_string = morse_string + " " + code_word
    morse_list.append(code_word)
print(f"Your code: {morse_string}")

# if choose_what == 'to_letter':
#     user_input = input('Enter a code: ').lower()
#     for reverse in range(len(user_input)):
#         reverse_letter = user_input[reverse]
#         reverse_keys = letter_codes[reverse_letter]
#         reverse_string = reverse_string + " " + reverse_keys
#     print(f"Your letter: {reverse_string}")







    # for reverse in range(len(user_input)):
    #     reverse_letter = user_input[reverse]
    #     reverse_keys = keys[vals.index(reverse_letter)]
    #     reverse_string = reverse_string + reverse_keys
    # print(reverse_string)
