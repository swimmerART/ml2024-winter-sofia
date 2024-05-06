class InputList:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def find_index(self, x):
        try:
            index = self.numbers.index(x) + 1
        except ValueError:
            index = -1
        return index
