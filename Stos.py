class Stos:
    def __init__(self):
        self.ilosc = []
    def push(self, ilosc):
        self.ilosc.append(self.ilosc)
    def is_empty(self):
        if len(self.ilosc) == 0:
            return print("Stos jest pusty")
        else:
            return print("Stos jest nie pusty")
    def top(self):
        return self.ilosc[-1]
    def pop(self):
        return self.ilosc.pop()

