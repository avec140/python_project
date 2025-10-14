# 파이썬을 잘 다루기 위한 나만의 프로그램 만들기
# chapter 1. 사칙연산 계산기 만들기

number = 0
while True:
     print("--------------------------")
     print("1. 덧셈")
     print("2. 뺄셈")
     print("3. 곱셈")
     print("4. 나눗셈")
     print("5. 종료")
     print("--------------------------")

     intro = int(input())

     if (intro == 1):
          print("첫번째 더하기할 숫자를 입력하세요")
          num1 = int(input())
          print("두번쨰로 더할 숫자를 입력하세요")
          num2 = int(input())
          result = num1 + num2
          print(f"더한 결과: {num1} + {num2} = {result}")

     elif (intro == 2):
          print("첫번째 뺄 숫자를 입력하세요")
          num1 = int(input())
          print("두번쨰로 뺄 숫자를 입력하세요")
          num2 = int(input())
          result = num1 - num2
          print(f"더한 결과: {num1} - {num2} = {result}")

     elif (intro == 3):
          print("첫번째 곱할 숫자를 입력하세요")
          num1 = int(input())
          print("두번쨰로 곱할 숫자를 입력하세요")
          num2 = int(input())
          result = num1 * num2
          print(f"더한 결과: {num1} * {num2} = {result}")

     elif (intro == 4):
          print("첫번째 나눌 숫자를 입력하세요")
          num1 = int(input())
          print("두번쨰로 나눌 숫자를 입력하세요")
          num2 = int(input())
          result = num1 // num2
          print(f"더한 결과: {num1} / {num2} = {result}")
     
     elif (intro == 5):
          break;     