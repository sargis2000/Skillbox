class Mydict(dict):

    def __init__(self, default=0):
        dict.__init__(self)
        self.default = default

    def get(self, key, *args):
        if not args:
            args = (self.default,)
        return dict.get(self, key, *args)


a = Mydict()
a[0] = 100
a[3] = 700
print(a.get(0))
print(a.get(790))
