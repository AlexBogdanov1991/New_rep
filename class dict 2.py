class MyDict:
    def __init__(self):
        self.data = []

    def __getitem__(self, key):
        for item in self.data:
            if item[0] == key:
                return item[1]
        return None

    def __setitem__(self, key, value):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def __delitem__(self, key):
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
        return str(self.data)

    def __contains__(self, key):
        for item in self.data:
            if item[0] == key:
                return True
        return False

my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])
print('city' in my_dict)
del my_dict['age']
print(my_dict.keys())
print(my_dict.values())