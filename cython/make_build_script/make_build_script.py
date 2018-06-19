# vim: set fileencoding=utf-8

from distutils import sysconfig
from sys import argv, exit

CC = "gcc"
CC_OPT = "-O9"

INCLUDE_DIR = sysconfig.get_python_inc()
LIBRARY_DIR = sysconfig.get_config_var('LIBDIR')
PYTHON_LIB = sysconfig.get_config_var('LIBRARY')[3:-2]
SYSTEM_LIBS = sysconfig.get_config_var('SYSLIBS')


if __name__ == "__main__":
    if len(argv) <= 1:
        print("usage: python make_build_script program_name > script.sh")
        exit(1)

    progname = argv[1]

    print("# very simple variant of the build script tied to specific Python version and an CPU architecture\n")  # noqa

    print("rm -f {progname}.c".format(progname=progname))
    print("rm -f {progname}\n".format(progname=progname))

    print("cython --embed {progname}.py\n".format(progname=progname))
    print("{cc} {cc_opt} -I {include_dir} -L{library_dir} -l{python_lib} {system_libs} {progname}.c -o {progname}".format(  # noqa
        cc=CC, cc_opt=CC_OPT, include_dir=INCLUDE_DIR, library_dir=LIBRARY_DIR,
        python_lib=PYTHON_LIB, system_libs=SYSTEM_LIBS, progname=progname))
