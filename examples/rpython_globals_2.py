x = []

def entry_point(argv):
    global x
    print x
    x.append(10)
    print x
    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
