# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.



while True:
    num = input("숫자를 입력하세요 : ")

    if num.isdigit() is False:
        print('정수가 아닙니다.')
        continue
    else:
        num = int(num)
        if int(num) % 2 == 0:
            for i in range(0, num):
                if i % 2 == 0:
                    i += i
                    print("결과 값 :", i+num-1)





num = int(num)
iseven = num & 0x0001 == 0
s = 0
for n in range(0,num +1):
    if iseven and n & 0x0001 == 0:
        s += n
    elif not iseven and n & 0x0001 ==1:
        s += n

print('결과 : ' , n)


