




# class MathDojo:
#     def __init__(self):
#         self.result = 0

#     def add(self, x, y):
#         xy = (x + y)
#         self.result += xy
#         return self

#     def subtract(self, a, b):
#         ab = (a + b)
#         self.result -= ab
#         return self

# md = MathDojo()

# print (md.add(1,2).add(2,5).subtract(3,2).result)



class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *yx):
        for loop in yx:
            if type(loop) == list:
                for j in loop:
                    self.result += j
            if type(loop) == int:
                self.result += loop
            if type(loop) == tuple:
                for u in loop:
                    self.result += u
        return self

    def subtract(self,*ab):
        for g in ab:
            if type(g) == list:
                for h in g:
                    self.result -= h
            if type(g) == int:
                self.result -= g
            if type(g) == tuple:
                for e in g:
                    self.result -= e
        return self

md = MathDojo()

print (md.add(1,2,3,(1,2,3)).result)
