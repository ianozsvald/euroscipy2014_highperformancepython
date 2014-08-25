from distutils.core import setup
from Cython.Build import cythonize

# basic setup but no openmp
setup(
    ext_modules = cythonize("cythonfn.pyx")
)
