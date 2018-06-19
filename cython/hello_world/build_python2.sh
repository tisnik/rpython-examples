# very simple variant of the build script tied to specific Python version and an CPU architecture

rm -f hello_world.c
rm -f hello_world

cython --embed hello_world.py

gcc -O9 -I /usr/include/python2.7 -L/usr/lib64 -lpython2.7 -lm hello_world.c -o hello_world
