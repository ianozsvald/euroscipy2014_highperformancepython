from distutils.core import setup
from Cython.Build import cythonize

from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_module = Extension(
    "cythonfn",
    ["cythonfn.pyx"],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
)

setup(
    name = 'Cython fn',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext_module],
)
