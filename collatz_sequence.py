from ter import *
while True:
    num=int(input("Enter your number: "))
    num = decimal_to_ternary(num)
    res =''
    count = 0
    while True:
        if not parity_check(num):
            res = mul3add1(num)
            count+= 1
            print(res,'multiplied', ternary_to_decimal(res),'\n')
            num = res
        if parity_check(num):
            res = divide_by_2(num)
            count += 1
            print(res, 'divided', ternary_to_decimal(res),'\n')
            num = res
