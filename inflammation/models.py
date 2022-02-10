"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.

Functions:
    load_csv - returns the contents of a file
    daily_mean - returns the mean value for each day
    daily_max - returns the maximum value for each day
    daily_min - returns the minimum value for each day
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV.

    :param filename: Filename of CSV to load
    :returns: the contents of a file as a np.array
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    
    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)
    :returns: an array holding the mean value for each day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    
    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)
    :returns: an array holding the maximum value for each day
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    
    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)
    :returns: an array holding the minimum value for each day
    """
    return np.min(data, axis=0)

