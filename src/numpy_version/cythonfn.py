import numpy as np

def calculate_z(maxiter, zs, cs, output):
    """Calculate output list using Julia update rule"""
    length = len(zs)
    for i in xrange(length):
        z = zs[i]
        c = cs[i]
        output[i] = 0
        while output[i] < maxiter and abs(z) < 2:
            z = z * z + c
            output[i] += 1
    return output
