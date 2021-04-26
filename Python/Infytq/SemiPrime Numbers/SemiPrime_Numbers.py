def isPrime(num):
	i = 2
	for i in range(2,num):
		if num%i==0:
			return False
	return True

tc = int(input())

for case in range(tc):

	n = int(input())

	primes = set()

	if n >= 2:
		primes.add(2)

	for num in range(2,n+1):
		if isPrime(num):
			primes.add(num)

	semiprimes = set()

	for i in primes:
		for j in primes:
			prod = i*j
			if prod <= n: 
				semiprimes.add(prod)

	for num in sorted(semiprimes):
		print(num, end = " ")
	print()
