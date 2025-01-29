class MyDict:
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        return self.data.get(key, None)
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]

    def keys(self):
        return list(self.data.keys())
    def values(self):
        return list(self.data.values())
    def items(self):
        return list(self.data.items())
    def __str__(self):
        return str(self.data)

    def __contains__(self, key):
        return key in self.data

my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])
print('city' in my_dict)
del my_dict['age']
print(my_dict.keys())
print(my_dict.values())


