# 파이썬을 잘 다루기 위한 나만의 프로그램 만들기
# chapter 1. 사칙연산 계산기 만들기

#전역변수 선언
number=0; num1=0; num2=0; result = 0

def add(num1, num2):
     return (num1 + num2)

def sub(num1, num2):
     return (num1 - num2)

def mul(num1, num2):
     return (num1 * num2)

def div(num1, num2):
     return (num1 // num2)

while True:
     print("--------------------------")
     print("1. 덧셈")
     print("2. 뺄셈")
     print("3. 곱셈")
     print("4. 나눗셈")
     print("5. 종료")
     print("--------------------------")

     intro = int(input())
     num1 = int(input("첫번째 숫자를 입력하세요 : "))
     num2 = int(input("두번째 숫자를 입력하세요 : "))

     if (intro == 1):
          result = add(num1, num2)
     elif (intro == 2):
          result = sub(num1, num2)
     elif (intro == 3):
          result = mul(num1, num2)
     elif (intro == 4):
          result = div(num1, num2)    
     elif (intro == 5):
          break;     

     print("결과 : ", result)