class Bird :
    def __init__(self):
        self.hungry = True
    def  eat(self):
         if self.hungry:
             print('Aaah')
             self.hungry =False
class  SongBird(Bird) :
    def __init__(self):
        # Bird.__init__(self)
        super().__init__()
        self.sound  =  'kkkk'
    def sing(self):
        print(self.sound)
songbird  = SongBird()
songbird.sing()
songbird.eat()