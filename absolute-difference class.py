

class Difference:
    def __init__(self, a):   #creates an object with
        self.__elements = a

    import itertools
    from itertools import combinations

    def generate_pairs(self,array):
        pairs_list = [(i,j) for i in array for j in array if i != j]
        return (pairs_list)
    def computeDifference(self):
        pairs_list = self.generate_pairs(self.__elements)

        abs_diff_list = [abs(pair[0] - pair[1])for pair in pairs_list]
        self.maximumDifference = max(abs_diff_list)
        return self.maximumDifference


#_ = input()
#a = [int(e) for e in input().split(' ')]
a = [1,2,3,5,6,6]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)