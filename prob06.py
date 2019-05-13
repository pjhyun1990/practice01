# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전,
# 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.


flag = 0

while flag == 0:


    money = input("금액:  ")
    change = 0
    money = int(money)

for won in [50000,10000,5000,1000,500,100,50,10,50,1]:
    count = money // won
    money -= count * won
    print('{0}원: {1}개'.format(won, count))





    if money / 50000 >= 1:
        change = money // 50000
        money = money - change * 50000

        print('50000원 : ', str(change)+ '개')

    if money / 10000 >= 1:
        change = money // 10000
        money = money - change * 10000
        print('10000원 : ', str(change) + '개')

    if money / 5000 >= 1:
        change = money // 5000
        money = money - change * 5000
        print('5000원 : ', str(change)+ '개')

    if money / 1000 >= 1:
        change = money // 1000
        money = money - change * 1000
        print('1000원 : ', str(change)+ '개')

    if money / 500 >= 1:
        change = money // 500
        money = money - change * 500
        print('500원 : ', str(change)+ '개')

    if money / 100 >= 1:
        change = money // 100
        money = money - change * 100
        print('100원 : ', str(change)+ '개')

    if money / 50 >= 1:
        change = money // 50
        money = money - change * 50
        print('50원 : ', str(change)+ '개')

    if money / 10 >= 1:
        change = money // 10
        money = money - change * 10
        print('10원 : ', str(change)+ '개')

    if money / 5 >= 1:
        change = money // 5
        money = money - change * 5
        print('5원 : ', str(change)+ '개')

    if money / 1 >= 1:
        change = money // 1
        money = money - change * 1
        print('1원 : ', str(change)+ '개')

