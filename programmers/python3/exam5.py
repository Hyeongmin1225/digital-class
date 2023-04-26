

#array = list(input("array : "))
#n = int(input("Input n : "))
def solution(arr, n):
    pair_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == n:
                pair_sum += arr[i] + arr[j]
    
    return pair_sum


print (solution([1,4,2,3,0,5],7))
print (solution([1,3,2,4],5))