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

