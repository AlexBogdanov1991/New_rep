class MyDict:
    def __init__(self):
        self.data = []

    def getitem(self, key):
        for item in self.data:
            if item[0] == key:
                return item[1]
        return None

    def setitem(self, key, value):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def delitem(self, key):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                del self.data[i]
                return

    def keys(self):
        return [item[0] for item in self.data]

    def values(self):
        return [item[1] for item in self.data]

    def items(self):
        return [(item[0], item[1]) for item in self.data]

    def __str__(self):

        items = ', '.join(f"{repr(key)}: {repr(value)}" for key, value in self.data)
        return f"{{{items}}}"

    def contains(self, key):
        for item in self.data:
            if item[0] == key:
                return True
        return False


my_dict = MyDict()
my_dict.setitem('name', 'Alice')
my_dict.setitem('age', 30)
print(my_dict.getitem('name'))
print(my_dict.contains('city'))
my_dict.delitem('age')
print(my_dict.keys())
print(my_dict.values())
print(my_dict)
