class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=max(candies)
        b=[]
        c=[]
        for i in range(len(candies)):
            b.append(candies[i]+extraCandies)
        for i in b:
            if i>=a:
                c.append(True)
            else:
                c.append(False)
        return c