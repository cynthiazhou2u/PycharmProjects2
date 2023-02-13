print(3>4)
print(5>=5)
print(6==7)
print(8==8)
print(9!=7)

age=9    #initialization of variable age
if age>10:
    print('it seems you are old')
elif age==200:
    print('hmm, you must come from another planet! you are at  wonder age')
else:
    print('you need to eat more porridge')

age=200
if age<10:
    print('you need to eat more porridge')
elif age==200:
    print('you are from another planet')
else:
    print('it seems you are old')


print(3>5)
print(3<5)
print(6<=9)
print(10>2)
print(10<2)
print(24>=23)
print(5==5)
print(5!=5)
print(5!=6)

#check string values
expected_title='CCTB-welcome!'
actual_title='CCTB'
print(expected_title==actual_title)
print(expected_title!=actual_title)

age=15
your_age= int(input('Please enter your age: '))
if age>your_age:
    print(f"Your age {your_age} is less than  {age}")
elif age <your_age:
    print(f"Your age {your_age} is greater than  {age}")
else:
    print(f"we don't know what your age is please try again")

print(f'welcome to our website to choose a game')
age=int(input('please enter your age: '))

if age>20 and age <=40:
    print(f'your age is {age}. not bad! you can play the following games: G1, G2, G3')
elif age > 11 and age <=20:
    print(f'your age is {age}. cool! we suggest these games: G4m G5m G6 ')
elif age > 5 and age<=11:
    print(f'your age is {age}. Awesome! Let\'s play these games: G7,G8,G9')
elif age==0:
    print("you're not born yet. please wait for a few years")
else:
    print(f"we don't have nay games for your age:{age}")

for x in range(0,4):             # start at 0, stop at 4 which means before or ahead of 4
    print(f'Hello, time {x}')               # initialize 0, check if less than upper limit; increment the value by 1, and check if less than upper limit...
for x in range(-3,0):             # this print 3 lines
    print(x)
for x in range(0,-1):                # this prints nothing
    print (x)
for x in range(0,0):               # this prints nothing
    print(x)

x=0
y=10
while x<y:
    x=x+3
    print(x)
x=0
while x<y:
    print(x)
    x+=3
    print(x)



