def f(param):
    if param:
        return 42
    else:
        return "foobar"


def entry_point(argv):
    z = f(True)
    print z

    w = f(False)
    print w

    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
