class ClassX:
    def foo(self):
        print("ClassX.foo")


class ClassY:
    def foo(self):
        print("ClassY.foo")


def entry_point(argv):
    obj = ClassX() if len(argv) == 2 else ClassY()
    obj.foo()
    return 0


def target(driver, args):
    return entry_point, None
