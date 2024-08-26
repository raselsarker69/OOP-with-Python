# set----> {}
# tuple----> ()
# List----> []
# set----> is a unique collection of items


numbers=[10,20,30,40,50,60,70,80,90,100]
print(numbers)

numbers_set=set(numbers)
print(numbers_set)

numbers_set.add(500)
print(numbers_set)

numbers_set.remove(50)
print(numbers_set)

for item in numbers_set:
    print(item)

    if 100 in numbers_set:
        print('100 exists')

    elif 25 in numbers_set:
        print('25 exists')

