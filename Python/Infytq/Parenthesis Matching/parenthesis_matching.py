word = input()

stack = []
balanced = True

for i in range(len(word)):
	element = word[i]
	if element in '[({':
		stack.append(element)
	if element in '})]':
		if len(stack) == 0:
			print(i+1)
			balanced = False
			break
		top = stack[-1]
		if ((top+element) in ['()','{}','[]']):
			stack.pop(-1)
		else:
			print(i+1)
			balanced = False
			break

if len(stack) > 0 and balanced:
	print(len(word)+1)
elif balanced:
	print(0)





