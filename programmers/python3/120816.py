def solution(slice, n):
    result = 0
    if n % slice != result :  
        result = n//slice + 1
    else :
        result = n//slice
    return result


print(solution (7,10))
print(solution (4,12))
