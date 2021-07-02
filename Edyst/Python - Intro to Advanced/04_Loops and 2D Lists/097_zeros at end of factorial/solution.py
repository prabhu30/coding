class Solution:
    def Met(self, n):
        # write your method here
        x = n // 5
        y = x 
        while x > 0:
            x /= 5
            y += int(x)
        print(y)
