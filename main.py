import sys
from calculator import add, subtract, multiply, divide


def get_numbers():
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the first number: '))
    return first_number, second_number


if __name__ == '__main__':
    try:
        print('Press CTRL + C to exit\n')

        while True:
            operation = int(input('1 - Addition\n2 - Subtraction\n3 - Multiplication\n'
                                  '4 - Division\nChoose an operation: '))

            if operation == 1:
                first_number, second_number = get_numbers()
                print(f'The addition of {first_number} and {second_number} '
                      f'is {add(first_number, second_number)}\n')

            elif operation == 2:
                first_number, second_number = get_numbers()
                print(f'The subtraction of {first_number} and {second_number} '
                      f'is {subtract(first_number, second_number)}\n')

            elif operation == 3:
                first_number, second_number = get_numbers()
                print(f'The multiplication of {first_number} and {second_number} '
                      f'is {multiply(first_number, second_number)}\n')

            elif operation == 4:
                first_number, second_number = get_numbers()
                print(f'The division of {first_number} and {second_number} '
                      f'is {divide(first_number, second_number)}\n')

            else:
                print(f'{operation} is not a valid option\n')

    except KeyboardInterrupt:
        print('Exit')
        sys.exit(0)

    except Exception:
        print('An unexpected error has occurred')
        sys.exit(1)
