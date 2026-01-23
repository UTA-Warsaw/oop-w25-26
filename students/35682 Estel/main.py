class Cat:
    total_count = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        type(self).total_count += 1

c1 = Cat("Whiskers", "black")
c2 = Cat("Yasna", "white")
c3 = Cat("Happy", "orange")


