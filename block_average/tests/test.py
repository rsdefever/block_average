# coding: utf-8

import numpy as np
import math

from block_average import block_average


def main():

    # Enter details here
    n_samples = [int(2.5e5)]
    # n_samples = [int(5e5),int(1e6),int(2e6),int(4e6)]

    for n_sample in n_samples:
        # Generate uncorrelated random samples
        uncorrelated_samples = np.random.normal(size=n_sample)

        average = np.mean(uncorrelated_samples)
        variance = np.var(uncorrelated_samples)

        # Calculate block averages and variances
        means_est, vars_est, vars_err = block_average(uncorrelated_samples)

        # Write output
        outfile = "uncorr_n{}_blkavg.out".format(n_sample)
        with open(outfile, "w") as f:
            f.write(
                "# Average: {:16.4f}, Variance: {:16.4f}\n".format(
                    average, variance
                )
            )
            f.write("# N_blk_ops, Mean_est, Var_est, var_err\n")
            for n_blk_ops, (mean_est, var_est, var_err) in enumerate(
                zip(means_est, vars_est, vars_err)
            ):
                f.write(
                    "{:10d}{:18.6f}{:16.4e}{:16.4e}\n".format(
                        n_blk_ops, mean_est, var_est, var_err
                    )
                )

        # Generate correlated random samples with MC walk
        moves = np.random.normal(0.0, 0.05, size=5 * n_sample)

        series = []
        pos = 0.0
        ener = energy(pos)
        for i in range(n_sample):
            series.append(pos)
            trial_pos = pos + moves[i]
            trial_ener = energy(trial_pos)
            if trial_ener < ener:
                pos = trial_pos
                ener = trial_ener
            else:
                rand = np.random.uniform()
                if math.exp(-(trial_ener - ener)) > rand:
                    pos = trial_pos
                    ener = trial_ener

        correlated_samples = np.asarray(series)
        # np.savetxt('correlated-samples.txt',correlated_samples)

        average = np.mean(correlated_samples)
        variance = np.var(correlated_samples)

        # Calculate block averages and variances
        means_est, vars_est, vars_err = block_average(correlated_samples)

        # Write output
        outfile = "corr_n{}_blkavg.out".format(n_sample)
        with open(outfile, "w") as f:
            f.write(
                "# Average: {:16.4f}, Variance: {:16.4f}\n".format(
                    average, variance
                )
            )
            f.write("# N_blk_ops, Mean_est, Var_est, var_err\n")
            for n_blk_ops, (mean_est, var_est, var_err) in enumerate(
                zip(means_est, vars_est, vars_err)
            ):
                f.write(
                    "{:10d}{:18.6f}{:16.4e}{:16.4e}\n".format(
                        n_blk_ops, mean_est, var_est, var_err
                    )
                )


def energy(x):
    return x ** 2


if __name__ == "__main__":
    main()
