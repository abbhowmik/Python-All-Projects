def add(num1, num2):
    print(f'The addition of this two number is : {num1 + num2}')


def substract(num1, num2):
    print(f'The substraction of this two number is: {num1 - num2}')


def multiplicate(num1, num2):
    print(f'The multiplication of this two number is : {num1 * num2}')


def divide(num1, num2):
    print(f'The division of this two number is : {num1/num2} ')


while True:
    print('***What you want to do right now?:: ')

    print(' 1. addition')
    print(' 2. substraction')
    print(' 3. multiplication')
    print(' 4. division')
    print('press 5 to Quit')

    try:
        a = input('Enter your choice:: ')
        num1 = int(input('Enter the first number:: '))
        num2 = int(input('Enter the second number:: '))

        if a == '1':
            add(num1, num2)
        elif a == '2':
            substract(num1, num2)
        elif a == '3':
            multiplicate(num1, num2)
        elif a == '4':
            divide(num1, num2)
        else:
            print('Thanks for using our calculator!')
            exit()

    except Exception as e:
        print(e)
