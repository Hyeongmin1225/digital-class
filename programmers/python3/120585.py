#머쓱이보다 키큰사람

# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
# 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.



#1번째줄 array, height 라는 변수를 설정하여
#2번째줄 결과 answer을 0으로 초기값을 주고
#3번째줄 for문에서 
# park hyeong min eun baboda.
# jabini parke morunun babo.kkk

def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

print(solution ([149, 180], 167))

