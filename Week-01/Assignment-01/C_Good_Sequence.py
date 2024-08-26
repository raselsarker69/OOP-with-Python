N = int(input())
nums = list(map(int, input().split()))

mp = {}  
for num in nums:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1

sum = 0

for key, value in mp.items():
    if value < key:
        sum += value
    elif value > key:
        sum += (value - key)

print(sum)