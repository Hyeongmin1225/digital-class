
#서로 다른 변수(n, r)를 입력 받아 순열이라는 연산 nPr로 계산

import math

n = int(input("n을 입력해주세요: "))
r = int(input("r을 입력해주세요: "))

if r <= n:
    permutation = math.factorial(n) / math.factorial(n-r)
    print("순열 n은", n, "순열 r은 ", r, "으로", permutation)
else:
    print("잘못된 입력 수")


