"""
The Effects of Outliers
=======================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script contains some useful functions.
"""

import math
import random

def roll_dice(n):
    """
    Simulates rolling a die *n* times.
    """
    experiment = [ random.randint(1, 6) for _ in range(n) ]
    return experiment

def joint_frequency(sample, x, y):
    """
    Find the joint frequecy of a sample of bivariate data { (x_i, y_i) } for a particular value of x and y.
    """
    freq = sum(1 for obs in sample if obs[0] == x and obs[1] == y)
    return freq

def sample_mean(sample):
    """
    Calculate the sample mean of a sample of data.
    """
    xbar = sum(sample) / len(sample)
    return xbar

def sample_percentile(sample, percentile):
    """
    Calculate the sample percentile of a sample of data.
    """
    sample.sort()
    n = len(sample)
    order = percentile * n
    order_floor = math.floor(order)
    order_ceiling = math.ceil(order)
    lower_bound = sample[order_floor]
    upper_bound = sample[order_ceiling]
    percentile_delta = (upper_bound - lower_bound)
    result = lower_bound + percentile_delta * (order - order_floor)
    return result
