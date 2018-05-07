class Rectangle:
    def __init__(self):
        self.width = 0

    def __setattr__(self, name, value):
        print('setattr')
        if name == 'size':
            print('222')
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        print('getattr')
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()


range = Rectangle()
range.height=4
# range.width=5
