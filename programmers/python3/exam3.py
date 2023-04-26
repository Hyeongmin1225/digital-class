
M_D = str(input("M - Multiply \nD - Division     Select: "))
x_data = int(input("Input Data x : "))
y_data = int(input("Input Data y : "))

def Multiply (num1,num2) :
    answer1 = 0
    answer1 = num1*num2
    return answer1


def Division (num1,num2) :
    answer = 0
    answer = num1//num2
    if answer != 0 :
        print("나머지가 나옴 오류!!")
    return answer
    



if M_D == 'm'or'M':
    print(Multiply(x_data,y_data))
elif M_D == 'd'or'D' :
    print(Division(x_data,y_data))
else:
    print("M이나 D를 입력해주세요")
