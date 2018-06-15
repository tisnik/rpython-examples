def entry_point(argv):
    l1 = [1, 2, 3, 4]
    l2 = ['a', 'b', 'c', 'd']
    l3 = [1, 'a']

    print l1
    print l2
    print l3

    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
