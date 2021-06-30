input1 = int(input())
input2 = list(map(int, input().split()))[:input1]

even = []
odd = []
srted = []

for i in input2:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)

even.sort()
odd.sort()

if len(even) < len(odd):
  small = len(even)
  rem = odd[small:]
else:
  small = len(odd)
  rem = even[small:]

mn = min(input2)
if mn%2==0:
  for i in range(small):
    srted.append(even[i])
    srted.append(odd[i])
  srted.extend(rem)
else:
  for i in range(small):
    srted.append(odd[i])
    srted.append(even[i])
  srted.extend(rem)

print(srted)
