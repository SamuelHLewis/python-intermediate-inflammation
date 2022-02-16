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

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised