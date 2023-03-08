# Student name: Jessica Lourenco
# Student name: Edison Forero

def encode(pwrd):
    encrypted_pwrd = ''

    for n in pwrd:
        num = (int(n) + 3) % 10
        encrypted_pwrd += str(num)

    return encrypted_pwrd


def decode(pwrd):
    decoded_pwrd = ''

    for n in pwrd:
        num = (int(n) - 3) % 10
        decoded_pwrd += str(num)

    return decoded_pwrd


def print_menu():
    print('Menu \n-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


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
            print()

        # decoding password
        if option == 2:
            print(f'The encoded password is {encrypted_pwrd}, and the original password is {pwrd}.')
            print()

    exit()  # option 3


if __name__ == '__main__':
    main()
