print(int(input('please enter an integer: ')))

user_entry=None

while type(user_entry) != int:
    try:
        user_entry=(input('Please enter an integer: '))
        user_entry=int(user_entry)
        print(f'you entered integer: {user_entry}. Program finished')
    except ValueError as err:
        print(f'U entered incorrect value: {user_entry}, please try again..')
        print(f'error message: {err}')

try:
    x=int(input('enter numerator: '))
    y=int(input('enter denominator: '))
    print(f'answer is :  {round(x/y)}')
except ZeroDivisionError as zeroerr:
    print(f'U can\'t divide by zero = {zeroerr}')
except ValueError as valerr:
    print(f'U entered a non-inter value - {valerr}')
finally:
    print('the program is done!')

try:
    twilight_saga=['twilight','new moon','eclipse','breaking dawn']
    print(twilight_saga)
    print(f'print item #4: {twilight_saga[3]}')
    print(f'print item #4: {twilight_saga[4]}')
except IndexError as ie:
    print(f'Index is incorrect - {ie}, check your item index')
finally:
    print(
        'done'
    )

#check number range
number=None
valid_flag=False
print(type(valid_flag))

while not valid_flag:
    try:
        number=int(input(f'please enter integer number from 1 to 10: '))
        while 0<number<=10:
            print(f'all good. Your number {number} is from 1 to 10')
            print('done')
            valid_flag=True
            break
        else:
            print(f'you number {number} is not from a given range. Please try again' )
    except ValueError as error:
        print(f'U entered a non integer value. Please try again. Error message{error}')

number=None
valid_flag=True
print(type(valid_flag))

while valid_flag:
    try:
        number=int(input(f'please enter integer number from 1 to 10: '))
        while 0<number<=10:
            print(f'all good. Your number {number} is from 1 to 10')
            print('done')
            valid_flag=False
            break
        else:
            print(f'you number {number} is not from a given range. Please try again' )
    except ValueError as error:
        print(f'U entered a non integer value. Please try again. Error message{error}')
