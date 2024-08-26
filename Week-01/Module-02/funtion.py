# define

def double_it(num):
    result = num * 2
    print(result)

double_it(5)
double_it(50)

def sum(num1 , num2):
    result = num1 + num2
    return result

total = sum(33, 44)
print('total value' , total)

def divided(num1 ,num2):
    result= num1 // num2
    # print(result)
    return result
result = divided(100,5)
print('total value' ,result)


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")
