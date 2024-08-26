def sum(nm1 ,nm2,nm3=0):
    result = nm1 * nm2 * nm3
    return result
total = sum(10, 30, 40)
print('total' , total)

# args

def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(sum)
        sum = sum + num
        return sum
total = all_sum(30)
print('all_sum',total)