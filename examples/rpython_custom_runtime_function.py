def muj_vstupni_bod_do_aplikace(argv):
    print "Hello world!"
    return 0

def target(driver, args):
    print "*** target ***"
    return muj_vstupni_bod_do_aplikace, None
