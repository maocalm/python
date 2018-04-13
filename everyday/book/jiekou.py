class Calculator :
    def calculate (self  , expression):
        self.value = eval(expression)

class Talker :
    def talk(self):
        print('hi, mu value is ' ,self.value )
class TalkingCalculator (Calculator ,Talker):
    pass


tc=  TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

print(hasattr(tc, 'talk'))
print(callable(getattr(tc, 'talk', None)))

print(tc.__dict__)



