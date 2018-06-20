class SuperClass:
    pass

class ClassX(SuperClass):
    def foo(self):
        print("ClassX.foo")


class ClassY(SuperClass):
    def foo(self, dummy):
        print("ClassY.foo")


def entry_point(argv):
    obj = ClassX() if len(argv) == 2 else ClassY()
    assert isinstance(obj, ClassX)
    obj.foo()
    return 0


def target(driver, args):
    return entry_point, None
