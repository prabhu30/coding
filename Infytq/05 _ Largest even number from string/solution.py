word = input()
num = ""
for element in word:
	if element in '0123456789':
		num = num + element

num = list(set(num))

if len(num) == 0:
	print(-1)
elif (('0' not in num) and ('2' not in num) and ('4' not in num) and ('6' not in num) and ('8' not in num)):
	print(-1)
else:
	num.sort(reverse = True)
	if(int(num[-1])%2==0):
		ans = ''.join(num)
		print(ans)
	else:
		smallest_even = num[-1]
		for digit in num:
			if int(digit)%2 == 0:
				smallest_even = digit
		num.remove(smallest_even)
		num.append(smallest_even)
		ans = ''.join(num)
		print(ans)
