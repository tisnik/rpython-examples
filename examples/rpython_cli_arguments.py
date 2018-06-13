def entry_point(argv):
    print "Command line arguments:"
    for arg in argv:
        print arg
    return 0

def target(driver, args):
    print "*** target ***"
    return entry_point, None
