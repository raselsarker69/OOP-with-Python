



add = lambda x, y : x + y
sum = add(50,50)
# print(sum)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
doubled_nums = map(lambda x: x*2, numbers)
squard_nums = map(lambda x: x*x, numbers)

print(numbers)
print(list(doubled_nums))
print(list(squard_nums))


actors = [
       
       {'name' : 'Tamim' , 'age': '35'},
       {'name' : 'Tamzim' , 'age': '40'},
       {'name' : 'Tanzid' , 'age': '45'},
       {'name' : 'Taizul' , 'age': '50'},
       {'name' : 'Rasel' , 'age': '55'},
       {'name' : 'Rafiya' , 'age': '60'},
       {'name' : 'Sakib' , 'age': '65'},
       
]


juniors = filter(lambda actor : actor['age'] < 40 , actors)
Fivers = filter(lambda actor : actor['age'] < %5==0 , actors)

print(list(juniors))
print(list(Fivers))