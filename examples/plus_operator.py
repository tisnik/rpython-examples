class Foo:
    def __init__(self, value):
        self._value = value

    def __add__(self, other):
        return Foo(self._value + other._value)

    def __str__(self):
        return str(self._value)



def entry_point(argv):
    f1 = Foo(1)
    f2 = Foo(2)

    f3 = f1 + f2

    print(f1)
    print(f2)
    print(f3)

    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
