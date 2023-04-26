

def M_m(array):
    answer = 0
    array.sort()
    answer = array[-1] - array[0]
    return answer



print(M_m ([23,3,19,21,16]))
print(M_m ([1,434,555,34,112]))