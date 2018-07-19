# very simple variant of the build script tied to Python 3.6 and x86-64 architecture

rm -f mandelbrot_python.c
rm -f mandelbrot_python

cython --embed mandelbrot_python.py

gcc -O9 -I /usr/include/python3.6m/ -L/usr/lib64 -lpython3.6m mandelbrot_python.c -o mandelbrot_python
