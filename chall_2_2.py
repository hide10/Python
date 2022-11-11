class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size


a_square = Square(20)
print(a_square.calculate_perimeter())

a_square.change_size(-2)
print(a_square.calculate_perimeter())
