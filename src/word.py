import string
class Word(object):
    def __init__(self) -> None:
        super().__init__()
        self.l1 = Letter(1)
        self.l2 = Letter(2)
        self.l3 = Letter(3)
        self.l4 = Letter(4)
        self.l5 = Letter(5)
        self.letterlist = [self.l1,self.l2,self.l3,self.l4,self.l5]
        self.grey = []
        self.required = []

    def __str__(self):
        print([(str(x)) for x in self.letterlist])
        return f"Banned letters = {self.grey}"


class Letter(object):
    def __init__(self,position) -> None:
        super().__init__()
        self.position = position
        self.letterlist = [x for x in 'etaoinsrhdlucmfywgpbvkxqjz']
    def __str__(self):
        return f"Letter in position {self.position}. Available letters = {self.letterlist}\n"