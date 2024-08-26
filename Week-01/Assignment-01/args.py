 
# *args example

def all_sum(*numbers):
    print(numbers)
    total_sum = 0 
    for arg in numbers:
        print(arg)
        total_sum = total_sum + arg  
    return total_sum

total = all_sum(50)
print('all sum:', total) 
       



#**kwargs example

def full_name(first, last):
    name = f'Full name is: {first} {last}'
    return name

name = full_name('Rasel', 'Sarker')
print(name)




