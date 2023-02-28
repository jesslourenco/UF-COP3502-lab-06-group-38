# Student name: Jessica Lourenco

def encode():
    

def print_menu():
    print('Menu \n-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def main():
    option = 0
    encrypted_pwrd = ''

    while option != 3:
        print_menu()
        option = int(input('Please enter an option: '))

        if option == 1:
            pwrd = input('Please enter your password to encode: ')
            encrypted_pwrd = encode(pwrd)
            print('Your password has been encoded and stored!')

        if option == 2:
            pass

        if option == 3:
            break

    exit()
        
if __name__ == '__main__':
    main()