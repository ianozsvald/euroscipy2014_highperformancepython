
To get this code
================

Clone this repository

    $ git clone git@github.com:ianozsvald/euroscipy2014_highperformancepython.git

Installation
============

We'll use Python 2.7, numpy and Cython. Installing with Anaconda (http://continuum.io/downloads) is easiest:

    $  ~/anaconda/bin/conda create -n euroscipy_2014_highperformancepython anaconda python=2.7 numpy cython
    $ source activate euroscipy_2014_highperformancepython

Note that you might have an error with libjpeg on Ubuntu machines, this is noted in the Anaconda forum and I don't have a solution for it. It means you can't run the visual output but you won't need it.

    Bug noted here: https://groups.google.com/a/continuum.io/forum/#!msg/anaconda/L28s5-qbFL8/oHaHUInZHLAJ

You'll want line_profiler and memory_profiler if you want to replicate the profiling:

    $ pip install memory_profiler
    $ pip install psutil

    # Get line_profiler's source from here
    # https://pypi.python.org/packages/source/l/line_profiler/line_profiler-1.0b3.tar.gz#md5=63fc2a757192eb5e577559cfdff5b831
    $ wget https://pypi.python.org/packages/source/l/line_profiler/line_profiler-1.0b3.tar.gz#md5=63fc2a757192eb5e577559cfdff5b831
    $ tar -xvf line_profiler-1.0b3.tar.gz
    $ python setup.py install

Note for Ian (teacher), use virtualenv rather than Anaconda to display the Pillow output:

    $ . ~/workspace/high_performance_python_book/high_performance_python_orielly/shared_github/raw_code/ian/envian/bin/activate

