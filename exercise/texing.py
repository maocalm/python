class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self ,size):
        self.width ,self.height =size
    def get_size(self):
        return  self.width ,self.height
    size = property(get_size ,set_size   #参数没有限制； 没有就是没有不可读， 不可写 ，
rect = Rectangle()
print(rect.size)
rect.size =  100 ,399
print(rect.size)
