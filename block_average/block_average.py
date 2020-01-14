# coding: utf-8

author = "Ryan DeFever"
modified = "2020-01-09"

import numpy as np
import math

def block_average(data):
    """
    Calculate block averages

    Implements the technique of Flyvbjerg and Peterson
    J. Chem. Phys. 91, 461 (1989). Also described in
    Appendix D of Frenkel and Smit.

    The data should be provided as a numpy ndarray with
    shape=(npoints,). The function performs N blocking
    operations, where the block size is 2^N and the
    maximum number of blocking operations is determined
    from the number of points in ``data``

    Parameters:
    -----------
    data : numpy.ndarray, shape=(npoints,)
        numpy array with shape (npoints,) where npoints
        is the number of data point in the sample

    Returns:
    -------
    means, vars_est, vars_err

    means : np.ndarray, shape=(n_avg_ops,)
        mean values calculated from different numbers
        of blocking operations
    vars_est : np.ndarray, shape=(n_avg_ops,)
        estimates of the variances of the average from different
        numbers of blocking operations
    vars_err: np.ndarray, shape=(n_avg_ops,)
        estimates of the error in the variances from different
        numbers of blocking operations
    """

    try:
        data = np.asarray(data)
    except:
        raise TypeError('data should be provided as a numpy.ndarray')

    means = []
    vars_est = []
    vars_err = []

    n_samples = data.shape[0]

    max_blocking_ops = 0
    block_length = 1
    while block_length < 1./4.*n_samples:
        max_blocking_ops += 1
        block_length = 2**max_blocking_ops

    # Calc stats for mulitple-of-two block lengths
    for m in range(max_blocking_ops):
        block_length = 2**m # Number of datapoints in each block
        n_blocks = int(n_samples/block_length) # Number of blocks we can get with given block size
        # Calculate the 'new' dataset by block averaging
        block_data = [ np.mean(data[i*block_length:(i+1)*block_length], dtype=np.float64) for i in range(n_blocks) ]
        block_data = np.asarray(block_data, dtype=np.float64)
        # Calculate the mean of this new dataset
        mean = np.mean(block_data, dtype=np.float64)
        # Calculate the variance of this new dataset
        var = np.var(block_data, dtype=np.float64)
        var_err = math.sqrt(2.0*var**2./(n_blocks-1)**3.)

        # Save data for blocking op
        means.append(mean)
        vars_est.append(var/(n_blocks-1))
        vars_err.append(var_err)

    return np.asarray(means), np.asarray(vars_est), np.asarray(vars_err)


