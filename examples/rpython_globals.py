x = 42

def entry_point(argv):
    global x
    print x
    x *= 1
    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
