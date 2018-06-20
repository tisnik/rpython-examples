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

    f3 = f1.__add__(f2)

    print(f1.__str__())
    print(f2.__str__())
    print(f3.__str__())

    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
