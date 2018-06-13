def foo():
    print "FOO FOO FOO FOO FOO FOO FOO FOO FOO"


def bar():
    print "BAR BAR BAR BAR BAR BAR BAR BAR BAR"


def baz():
    print "BAZ BAZ BAZ BAZ BAZ BAZ BAZ BAZ BAZ"


def entry_point(argv):
    print "Hello world!"
    foo()
    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
