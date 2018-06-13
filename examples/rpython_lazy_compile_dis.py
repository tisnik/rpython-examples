import dis

def foo():
    print "FOO FOO FOO FOO FOO FOO FOO FOO FOO"


def bar():
    print "BAR BAR BAR BAR BAR BAR BAR BAR BAR"


def baz():
    print "BAZ BAZ BAZ BAZ BAZ BAZ BAZ BAZ BAZ"


def main():
    print "Hello world!"
    foo()
    return 0

print "main"
dis.dis(main)

print "\nfoo"
dis.dis(foo)

print "\nbar"
dis.dis(bar)

print "\nbaz"
dis.dis(baz)
