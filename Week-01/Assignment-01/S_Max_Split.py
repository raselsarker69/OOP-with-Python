s = input()
L = 0 
R = 0  
cur_string = ""
new_string = []

for char in s:
    if char == "L":
        L += 1
    else:
        R += 1

    cur_string += char

    if L == R:
        new_string.append(cur_string)
        cur_string = ""

print(len(new_string))

for string in new_string:
    print(string)

