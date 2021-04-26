class Solution:
    def countItems(self, Aname, Aprice, Bname, Bprice):
        # write your method here
        c = 0
        for i in Aname:
            Aind = Aname.index(i)
            if i in Bname:
                Bind = Bname.index(i)
                if (Aprice[Aind] != Bprice[Bind]):
                    c += 1
        
        return c
        
s = Solution()
result = s.countItems([ "code", "fode", "mode" ],[3, 2, 1],[ "code", "fode", "mode", "load" ],[4, 2, 2, 2])
print(result)
