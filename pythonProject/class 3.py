a=[1,2,3,'a',1,3,5]   #create list
print(a)
print(tuple(a))
print(set(a))

b={'a',1,4,8}  #create set
print(b)
print(list(b))
print(tuple(b))

print(True * 2)    #1 *2
print(False *2)       # 0*2
print(75*8)

print(2**5)
print(100/2)
print(99//2)

print(10%3)
print(10%4)
print(15%12)

#print(100/0)

print(7+56*(13+11)/3**3)
print(6*4-(10/2)**3)
print(156*51-(10/2)**3)

list_of_names =[]
list_of_names=['Luke','Leia','Aniken','Padme','Han','Ben']
print(list_of_names)

print(list_of_names[0]) # list index starts with 0
print(list_of_names[5])

list_of_names[4]='Rey'
print(list_of_names)

list_of_names.append('Han Solo')
print(list_of_names)

list_of_names.pop(2)  #remove  item of index 2 - starting 0
print(list_of_names)

tropical_list=['Durain','mangosteen','jackfruit','cherimoya','lychee']
print(tropical_list)

for fruit in tropical_list:
    print(fruit)

yummy_tupple=('apple','pear','plum','grapes')
print(yummy_tupple)

for f in yummy_tupple:
    print(f)

print(yummy_tupple[1])
print(yummy_tupple[0])
#print(yummy_tupple.append('watermelon'))  --- error

yummy_list=list(yummy_tupple)
yummy_list.append('watermelon')
yummy_list.append('watermelon')
print(yummy_list)
print(yummy_list.append('watermelon'))  # none is produced by print
yummy_list.pop(2)
print(yummy_list)
yummy_tupple = tuple(yummy_list)
print(yummy_tupple)

yummy_set={'apple','pear','plum','grapes','watermelon'}
print(yummy_set)

for ys in yummy_set:
    print(ys)

#dictionary student ,
student={
    'name' : 'John Smith',
    'cohort': 3,
    'year': 2021,
    'grade':100
}
print(student)
new_user = {
    'username': 'testuser999',
    'password':'Pass1',
    'firstname': 'Test',
    'lastname':'User999',
    'email': 'tesetuser999@yahoo.com'
}
print(new_user)

print(student.keys())
print(new_user.keys())
print(student.values())
print(new_user.values())

print(student.get('cohort'))
print(new_user.get('password'))
student.update({'year':2022})    # update dictionary
print(student)
new_user.update({'password':'Pwd3!'})
print(new_user)

student['name']='James Cook'     # update dictionary method2
new_user['username']='happyuser999'
print(student)
print(new_user)

a=[1,2,3,'a',1,3,5]
print(a)
print(tuple(a))
print(set(a))
b={'a',1,3,4}
print(b)
print(list(b))
print(tuple(b))