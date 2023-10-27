encoded_password = None


def encode():  # Encode Function
    global encoded_password  # Calls global variable to change

    user_input = input('Please enter your password to encode: ')

    result = ''
    for i in user_input:  # Adds 3 to each digit and subtracts 10 if 'i' ends up multi-digit

        i = int(i) + 3

        if i >= 10:
            i = i - 10

        i = str(i)  # returns i to a string and attaches it to the result string
        result += i

    encoded_password = result  # changes the global variable of encoded_password for future reference in decode()

    return result


__name__ = '__Main__'

if __name__ == '__Main__':

    while True:  # This is the main loop where the menu is created and the user interacts with the program

        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        choice = input('Please enter an option: ')

        if choice == '1':
            encode()
            print('Your password has been encoded and stored!\n')

        '''if choice == '2':
            print(f'The encoded password is {encoded_password}, and the '
                  f'original password is {decode()}.\n')'''

        if choice == '3':
            break
