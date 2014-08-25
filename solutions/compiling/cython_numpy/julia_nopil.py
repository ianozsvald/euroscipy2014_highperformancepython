"""Julia set generator without optional PIL-based image drawing"""
import time
import numpy as np
from cythonfn import calculate_z


# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193


def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex co-ordinates (zs) and complex parameters (cs), build Julia set and display"""
    # Old co-ord building approach
    #zs = []
    #for ycoord in y:
        #for xcoord in x:
            #zs.append(complex(xcoord, ycoord))
    ## convert our Python lists into numpy array
    ## whilst preserving their order
    ## (this is quite verbose...)
    #zs_np = np.array(zs, np.complex128)
    #del zs

    # another way of converting but doesn't preserve the same order
    # so the displayed output would be inverted
    #from itertools import product
    #zs_np = np.array([complex(*v) for v in product(x, y)])

    # Make linearly spaced lists to copy the Python behaviour
    axs = np.linspace(x1, x2, 1001)[:-1]
    ays = np.linspace(y2, y1, 1001)[:-1]
    # Create a grid of co-ordinates as two lists
    ax, ay = np.meshgrid(axs, ays)
    # Create a new complex item by combining the float items
    az = ax + 1j * ay
    # Flatten the 2D array back to a 1D co-ord list
    az = np.ravel(az)
    #assert (max(az - zs_np)) < 0.0000000001
    zs_np = az

    # Create the C constant grid
    # note that using empty is slightly faster than using zeros
    # as we're going to fill the grid anyhow
    cs_np = np.empty(1000000, dtype=np.complex_)
    cs_np.fill(complex(c_real, c_imag))

    # again we can use empty to make the grid as we're going to
    # overwrite the entries
    output = np.empty(len(zs_np), dtype=np.int64)

    print "Length of x:", len(ax)
    print "Total elements:", len(zs_np)
    start_time = time.time()
    output = calculate_z(max_iterations, zs_np, cs_np, output)
    end_time = time.time()
    secs = end_time - start_time
    print "Took", secs, "seconds"

    validation_sum = sum(output)
    print "Total sum of elements (for validation):", validation_sum


# Calculate the Julia set using a pure Python solution with
# reasonable defaults for a laptop
# set draw_output to True to use PIL to draw an image
calc_pure_python(desired_width=1000, max_iterations=300)
