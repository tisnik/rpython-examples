def entry_point(argv):
    print "Hello world!"
    return 0

def target(driver, args):
    print "*** target ***"
    return entry_point, None
