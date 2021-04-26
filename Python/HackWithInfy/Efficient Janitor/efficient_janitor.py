def getMinTrips (weight, n):
  
  weight.sort()
  left_index = 0
  trips = 0
  
  for i in range (n-1,-1,-1):
  
    if(weight[i]> 1.99):
      trips += 1
  
    elif (weight[i] <= 1.99):
  
      if(weight [1]+weight [left_index] <= 3):
        left_index += 1
      trips += 1
  
    if(left_index >= i):
      break
  
  return trips
  
n = int(input())
weight = list (map(float, input().split()))
trips = getMinTrips (weight, n)
print(trips)
