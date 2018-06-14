def entry_point(argv):
    x = "one"
    print x
    x = 2
    print x
    x = None
    print x
    x = True
    print x
    x = range(10)
    print x[1]
    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
