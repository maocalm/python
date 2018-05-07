class  Fiba:
    def __init__(self):
        self.a = 0
        self.b  = 1
    def __next__(self):
        self.a ,self.b = self.b , self.a +self.b
        return self.a
    def __iter__(self):
        return    self


fibs  = Fiba()
for f  in fibs:
    if f > 1000:
        print(f)
        break


it = iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))