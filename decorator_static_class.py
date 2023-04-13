class game:
    def __init__(self, hp):
        self.hp = hp

    def test(self):
        self.hi()

    @staticmethod    
    def s():
        print('staticmethod')

    @staticmethod    
    def hi():
        print('hi')

    @classmethod
    def c(cls):
        cls(100).test()

game.s() # staticmethod
game.c() # hi