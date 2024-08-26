sz = int(input())
nums = list(map(int, input().split()))

cnt = 0
mn = float('inf')
flag = True

for i in range(sz):
    if nums[i] % 2 != 0: 
        flag = False
        print(0)
        break
    else:
        cnt = 1
        nums[i] //= 2  

    while nums[i] % 2 == 0:
        cnt += 1
        nums[i] //= 2 

    mn = min(mn, cnt)

if flag:
    print(mn)