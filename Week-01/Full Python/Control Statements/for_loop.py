# numbers=[1,10]
# for num in numbers:
#     print(num)

#-----------prob_01-----------------
# for i in range(-100,-9):
#     print(i)

#-----------Prime Number-----------------

"""
start = int(input("Enter lowest value:"))
end = int(input("Enter highest value:"))
sum = 0

for i in range(start, end + 1):
    is_prime = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            is_prime = 0
            break

    if is_prime==1:
        sum+=i
print(f"Sum of all prime numbers between {start} to {end} = {sum}")
"""
#-----------------------factorial-----------------------
"""
n=int(input("Enter your number:"))
fact=1
if n<0:
    print("factorial of negative number does not exits!")
else:
    for i in range(1,n+1):
        fact*=i
print(fact)
"""       
#----------------------Reverse-------------------------

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10

# Display the reversed number
print("Reversed number:", reverse)