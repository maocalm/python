class Myclass :
    @staticmethod
    def smeth():
        print("this is a static method ")

    # @classmethod
    def cmeth(cls):
        print('this is a class meth')




Myclass.smeth()
myclass = Myclass()
myclass.cmeth()
