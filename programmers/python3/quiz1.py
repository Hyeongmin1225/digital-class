
# 프로그램 구현 [리스트]
# 리스트 변수 [...] 주어졌을 때 변수안의 짝수 합과 홀수 합
# 나타내는 프로그램 구현


def solution(number) :
    sum = 0
    sum1 = 0
    for i in number :
        if i%2 == 1 :
            sum = sum + i
        else :
            sum1 = sum1 +i
            
    return sum ,sum1


print(solution ([1,2,3,3,3,4]))