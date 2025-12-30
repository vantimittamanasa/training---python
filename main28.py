class overloadDemo:
    def multiply(self,a,b):
        print(a*b)
    def multiply(self,a,b,c):
        print(a*b*c)
m=overloadDemo()
m.multiply(5, 10)