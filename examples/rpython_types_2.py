def entry_point(argv):
    if True:
        x = "one"
    else:
        x = 42
    print x
    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
