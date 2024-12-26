fruits=['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]

print(fruits)
print(fruits[0])
print(fruits[1][0])
print(fruits[1][1])

menu=['dal','paneer','kofta','tawa paneer','rice','roti']
author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')
timing='It\'s 7.30am'

for i in range(len(menu)):
    print(menu[i])

for i in range(len(author_name)):
    print(author_name[i])

for i in range(len(timing)):
    print(timing[i])

val=[]
for i in range (3,16,3):
    val.append(i)
    print('display result:',*val)

val1=[]
for i in range (12,1,-3):
    val1.append(i)
    print('display result:',*val1)


name=input('enter employee name:')
salary=input('enter salary:')
company_name=input('enter company name:')

print(name,salary,company_name)

print('hello world')
print('E:\ChangepondNewBatch\python')

ins=[]
size=int(input('enter a size : '))
print('enter values')
for i in range(size):
    val=float(input())
    ins.append(val)
print('enter float values : ',ins)


ins1=[]
size=int(input('enter a size : '))
print('enter values')
for i in range(size):
    val=input()
    ins1.append(val)
print('enter float values : ',ins1)



menu=['dal','paneer','kofta','tawa paneer','rice','roti']
author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')
timing='It\'s 7.30am'

i=0
while(i<len(menu)):
    print(menu[i])
    i+=1

i=0
while(i<len(author_name)):
    print(author_name[i])
    i+=1

i=0
while(i<len(timing)):
    print(timing[i])
    i+=1 


fruits=['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]
print(fruits[1][0])
print(fruits[3][0])


menu=['dal','paneer','kofta','tawa paneer','rice','roti']
menu[3]='malai paneer'
print(menu)

menu[4:]='tandoori roti','naan'
print(menu)


data=input('Enter the num:')
print(sum([int(i) for i in data]))
