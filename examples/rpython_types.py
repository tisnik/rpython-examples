def entry_point(argv):
    if len(argv) == 1:
        x = "one"
    else:
        x = 42
    print x
    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
