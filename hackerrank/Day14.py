class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        maxim = []
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                x = abs(self.__elements[i] - self.__elements[j])
                maxim.append(x)

        self.maximumDifference = max(maxim)
    

            
            

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)