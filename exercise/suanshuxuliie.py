class ArithmeticSequence :
    def __init__(self , start =0 , step =1  ):
        self.start = start
        self.step = step
        self.change = {}
    def __getitem__(self, item):
        check_index(item)
        print('getitem')
        try:
            print('item'+str(item))
            return  self.change[item]  # 不符合规则 ， 为空拉
        except KeyError:
            print('erro')
            return  self.start +item * self.step
    def __setitem__(self, key, value):
        check_index(key)
        self.change[key] =value
        print('setitem')


def  check_index(key):
    if not isinstance(key ,int ):raise TypeError
    if key <0: raise  IndexError


s= ArithmeticSequence(1,2)
print(s[1])
#
# for a  in range(0,4):
#     print(s[a])


