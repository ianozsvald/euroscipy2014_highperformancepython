import numpy as np
cimport numpy as np

# to compile
# python setup.py build_ext --inplace

def calculate_z(int maxiter, double complex[:] zs,
                double complex[:] cs, long[:] output):
    """Calculate output list using Julia update rule"""
    cdef unsigned int i, length
    cdef double complex z, c
    #for i in range(len(zs)):
    length = len(zs)
    for i in xrange(length):
        z = zs[i]
        c = cs[i]
        output[i] = 0
        #while output[i] < maxiter and z.real*z.real+z.imag*z.imag < 4:
        while output[i] < maxiter and abs(z) < 2:
            z = z * z + c
            output[i] += 1
    return output
