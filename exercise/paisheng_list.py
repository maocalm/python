class CounterList(list):
    def __init__(self ,*args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, item):  #范文元素列表的时候调用
        self.counter+=1
        return  super(CounterList, self).__getitem__(item)

cl = CounterList(range(10))
print(cl)  #序列

print(cl.__getitem__(2))
del cl[3:6]
print(cl)

print(cl.counter)