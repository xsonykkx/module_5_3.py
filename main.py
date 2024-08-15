class House:
    def init(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(self.number_of_floors):
            print()
            return
        int(new_floor)
        if new_floor < 1:
            print("Такого этажа не существует")
        elif new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            print(new_floor)

    def len(self):
        return self.number_of_floors

    def str(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def eq(self, value):
        return self.number_of_floors == value

    def lt(self, value):
        return self.number_of_floors < value

    def le(self, value):
        return self.number_of_floors <= value

    def gt(self, value):
        return self.number_of_floors > value

    def ge(self, value):
        return self.number_of_floors >= value

    def ne(self, value):
        return self.number_of_floors != value

    def add(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += int(value)
        return self

    def radd(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def iadd(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # eq

h1 = h1 + 10  # add
print(h1)
print(h1 == h2)

h1 += 10  # iadd
print(h1)

h2 = 10 + h2  # radd
print(h2)

print(h1 > h2)  # gt
print(h1 >= h2)  # ge
print(h1 < h2)  # lt
print(h1 <= h2)  # le
print(h1 != h2)  # ne
