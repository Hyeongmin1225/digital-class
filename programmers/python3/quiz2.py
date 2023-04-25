

# 입력받은 10진수 숫자의 자리수를 출력하는 프로그램 작성
# 예) 숫자 : 2023
# 결과 : 4: 2, 3: 0, 2: 2, 1: 3



def solution(number):
    answer = list(map(int,str(number)))
    print("4:",answer[0])
    print("3:",answer[1])
    print("2:",answer[2])
    print("1:",answer[3])
    #print(3,answer[1])
    #print(2,answer[2])
    #print(1,answer[3])



number = input("숫자를 입력하시오: ")

num_digits = len(number)

for i in range(num_digits):
    print(num_digits-i, ":",number[i])

#print(solution (2023))