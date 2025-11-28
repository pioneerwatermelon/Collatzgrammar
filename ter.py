def decimal_to_ternary(number):
	if number==0:
    		return '0'
	digits = []
	num = number
	while num != 0:
		remainder = num % 3

		if remainder == 0:
			digits.append('0')
			num //= 3
		elif remainder == 1:
			digits.append('+')
			num //= 3
		elif remainder == 2:
			digits.append('-')
			num = (num+1)//3
	return "".join(reversed(digits))

def ternary_to_decimal(s):
	value = 0
	for digit in s:
		value *= 3
		if digit == "+":
			value += 1
		elif digit == "-":
			value -= 1
		elif digit == "0":
			pass
	return value

def flip(num):
    string=''
    for i in num:
        if i == '+':
            string +='-'
        elif i == '-':
            string += '+'
        else:
            string += i
    return string


def hetero(num):
    if num == '+-':
        return '0+'
    zero_count = num.count('0')
    return '0' + '+' * (zero_count+1)


def homo(num):
	zero_count = num.count('0')
	return '+'+ ('-' * (zero_count+1))

def transform(num):
    if num[-1]=='-':
        return hetero(num)
    elif num[-1] =='+':
        return homo(num)


def divide_by_2(num):
    e_parity=True
    string=''
    dividend=''
    for c in str(num):
        if c!='0':
            e_parity = not e_parity
        dividend+=c
        if e_parity and dividend[0] == '+':
            print(dividend, 'this is a dividend')
            string+=transform(dividend)
            dividend=''
        elif e_parity and dividend[0] == '-':
            print(dividend, 'this is a dividend')
            string += flip(transform(flip(dividend)))
            dividend=''
        elif e_parity and dividend[0]=='0':
            print(dividend, 'this is a dividend')
            string += '0'
            dividend = ''
    if e_parity == False :
        return "Number is not even"
    return string.lstrip('0')

def mul3add1(num):
    return num + '+'

def parity_check(num):
    even = True
    for i in str(num):
        if i !='0':
            even = not even
    return even
