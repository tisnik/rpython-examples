class SuperClass:
    pass

class ClassX(SuperClass):
    def foo(self):
        print("ClassX.foo")


class ClassY(SuperClass):
    def foo(self, dummy):
        print("ClassY.foo")


def entry_point(argv):
    obj = ClassX() if len(argv) == 1 else ClassY()
    assert isinstance(obj, ClassY)
    obj.foo("dummy")
    return 0


def target(driver, args):
    return entry_point, None
