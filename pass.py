from secrets import choice
from string import ascii_letters, digits, punctuation
from argparse import ArgumentParser

def gen_mnemonic(password):
    # open the words file
    with open("words.txt", "r") as f:
        words = [word.strip() for word in f.readlines()]
    # generate a mnemonic string
    mnemonic = ""
    for char in password:
        if char.isalpha():
            matching_words = [word for word in words if word.startswith(char)]
            if matching_words:
                mnemonic += choice(matching_words)
            else:
                mnemonic += char
        else:
            mnemonic += char
        mnemonic += " "
    return mnemonic.strip()

def gen_pwd(pwd_length):
    # generate a password string
    pwd = ''
    for i in range(pwd_length):
        pwd += choice(alphabet)
    return pwd

# parsing arguments
parser = ArgumentParser(description='Generator of mnemonics and passwords')
parser.add_argument("-n", "--num", metavar='', type=int, default=1,
                help='number of passwords to generate (example: 8)')
parser.add_argument('-l', '--length', metavar='', type=int, default=12,
                help='length of passwords to generate (example: 10)')
parser.add_argument('-a', '--alphabet', metavar='', type=str, default='l_d',
                help='alphabet to use, l/letters, d/digits, s/symbols (examples: l_d_s, letters_digits)')
args = parser.parse_args()
number_of_pwds = args.num
pwd_length = args.length
alphabet_parts = args.alphabet.split('_')
alphabet = ''
# definition of the alphabet
for part in alphabet_parts:
    if part == 'letters' or part == 'l':
        alphabet += ascii_letters
    elif part == 'digits' or part == 'd':
        alphabet += digits
    elif part == 'symbols' or part == 's':
        alphabet += punctuation
# output
for i in range(number_of_pwds):
    password = gen_pwd(pwd_length)
    mnemonic = gen_mnemonic(password)
    print(password)
    print(mnemonic)
