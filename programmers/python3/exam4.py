

A_data = int(input("Input Data A : "))
B_data = int(input("Input Data B : "))


count = 0 
answer = (A_data + B_data) // 2
while B_data >= A_data:
    count += 1
    if answer <= A_data :
        break
    if answer > A_data :
        B_data = answer
    else:
        A_data = answer 
    answer = (A_data + B_data) // 2
print(count)


