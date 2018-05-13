from common import ABC ,abstractclassmethod


class Talker (ABC):
    @abstractclassmethod
    def talk(self):
        pass
class Herring :
    # def talk(self):
    #     print('herring')

    pass

print(Talker.register(Herring))  # 导致可以实例化了； 本来没有重写talk方法不可以实例化的


h = Herring()

print(isinstance(h, Talker))


# <class '__main__.Herring'>

