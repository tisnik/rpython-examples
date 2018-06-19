PYTHON=python3
COMPILER=gcc
LINKER=gcc

# GCCOPTIONS=-O9 -ffast-math
CCOPTIONS=-O9

INCLUDE_DIR:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc())")
LIBRARY_DIR:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
PYTHON_LIB:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBRARY')[3:-2])")
SYSLIBS:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('SYSLIBS'))")


all: hello_world

hello_world: hello_world.o
	$(LINKER) -o $@ $^ -L$(LIBRARY_DIR) -l$(PYTHON_LIB) $(SYSLIBS)

hello_world.o: hello_world.c
	$(COMPILER) $(CCOPTIONS) -I$(INCLUDE_DIR) -c $<

hello_world.c: hello_world.py
	cython --embed $<

clean:
	rm -f hello_world
	rm -f hello_world.c
	rm -f hello_world.o
