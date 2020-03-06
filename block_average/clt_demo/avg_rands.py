# coding: utf-8

import numpy as np

sample_sizes = [3, 5, 10, 50]
n_samples = 5000000

bins = {}
bin_edges = np.arange(-2.5, 2.7, 0.005)

for size in sample_sizes:

    rands = np.random.uniform(low=-1.0, high=1.0, size=(n_samples, size))
    avgs = np.mean(rands, axis=1)
    bins[size], edges = np.histogram(avgs, bins=bin_edges, density=True)

with open("uniform.out", "w") as f:
    f.write("# Bin, counts (M=3,5,10,50)\n")
    for i in range(len(bin_edges) - 1):
        bin_center = (bin_edges[i] + bin_edges[i + 1]) / 2.0
        f.write("{:10.4f}".format(bin_center))
        for size in sample_sizes:
            f.write("{:10.5f}".format(bins[size][i]))
        f.write("\n")

######################################################################
######################################################################

# sample_sizes = [3,5,10,50]
# n_samples = 500000
#
# bins = {}
# bin_edges = np.arange(-2.5,2.7,0.1)
#
# for size in sample_sizes:
#
#    rands = np.random.uniform(size=(n_samples,size))
#    avgs = []
#    for j in range(rands.shape[0]):
#        isum=0
#        for i in range(rands.shape[1]):
#            if rands[j][i] < (1./2.):
#                val = rands[j][i]/2. - 2.
#            elif rands[j][i] < (3./4.):
#                val = rands[j][i]
#            else:
#                val = rands[j][i]/2. + 1.
#            isum += val
#        avgs.append(isum/size)
#
#    bins[size], edges = np.histogram(avgs,bins=bin_edges,density=True)
#
# with open('non-uniform.out','w') as f:
#    f.write('# Bin, counts (M=3,5,10,50)\n')
#    for i in range(len(bin_edges)-1):
#        bin_center = (bin_edges[i] + bin_edges[i+1])/2.
#        f.write('{:10.4f}'.format(bin_center))
#        for size in sample_sizes:
#            f.write('{:10.5f}'.format(bins[size][i]))
#        f.write('\n')
#
#
