def foo():
    print "FOO FOO FOO FOO FOO FOO FOO FOO FOO"
    bar()
    baz()


def bar():
    print "BAR BAR BAR BAR BAR BAR BAR BAR BAR"
    baz()


def baz():
    print "BAZ BAZ BAZ BAZ BAZ BAZ BAZ BAZ BAZ"


def aaa():
    print "AAA AAA AAA AAA AAA AAA AAA AAA AAA"


def bbb():
    print "BBB BBB BBB BBB BBB BBB BBB BBB BBB"


def ccc():
    print "CCC CCC CCC CCC CCC CCC CCC CCC CCC"


def entry_point(argv):
    print "Hello world!"
    foo()
    return 0


def target(driver, args):
    print "*** target ***"
    return entry_point, None
