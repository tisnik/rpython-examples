def entry_point(argv):
    t = ["a", "b", "c", "d"]

    for i in range(len(t)):
        print i, t[1:i:2]

    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
