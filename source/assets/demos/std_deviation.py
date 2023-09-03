
"""
Point Estimators
================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script illustrates how altering the sample distribution affects the value of the sample deviation.
"""


def sample_mean(sample):
	"""
	Calculate the sample mean of a sample of data.
	"""
	xbar = sum(sample) / len(sample)
	return xbar
	
def sample_std_deviation(sample):
	"""
	Calculate the sample standard deviation of a sample of data.
	"""
	n = len(sample)
	mean = sample_mean(sample)
	sum_squared_deviations = sum( (obs - mean)**2 for obs in sample )
	std_dev = math.sqrt(sum_squared_deviations / (n-1))
	return std_dev
