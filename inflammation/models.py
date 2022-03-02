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
from numpy import ndarray


def load_csv(filename: str) -> ndarray:
    """Load a Numpy array from a CSV.

    :param filename: Filename of CSV to load
    :returns: the contents of a file as a np.array
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data: ndarray) -> ndarray:
    """Calculate the daily mean of a 2D inflammation data array.
    
    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)
    :returns: an array holding the mean value for each day
    """
    return np.mean(data, axis=0)


def daily_max(data: ndarray) -> ndarray:
    """Calculate the daily max of a 2D inflammation data array.
    
    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)
    :returns: an array holding the maximum value for each day
    """
    return np.max(data, axis=0)


def daily_min(data: ndarray) -> ndarray:
    """Calculate the daily min of a 2D inflammation data array.
    
    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)
    :returns: an array holding the minimum value for each day
    """
    return np.min(data, axis=0)


def daily_sd(data: ndarray) -> ndarray:
    """Calculate the standard deviation for each column of a 2D inflammation data array
    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)
    :returns: an array holding the sd value for each day
    """
    return np.std(data, axis=0)

def patient_normalise(data: ndarray) -> ndarray:
    """Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0

    :param data: a 2D data array with inflammation data
                 (rows are patients, columns are days)

    :returns: an array with normalised value
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    if not isinstance(data, np.ndarray):
        raise TypeError('Input data should be a numpy ndarray')
    if not len(data.shape) == 2:
        raise ValueError('Input data should be 2 dimensional')
    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


class Observation:
    """An object that holds basic information about patient

    :param day: day of measurement for a patient
    :param value: value of measurement for a patient
    """
    def __init__(self, day: int, value: int) -> None:
        self.day = day
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Person:
    """A general-purpose parent class for any objects representing people

    :param name: a name of the person
    """
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

class Patient(Person):
    """A patient in an inflammation study.

    :param name: name of the patient
                 (parameter inherited from class Person)
    :param observation: list of observation points for a given patient
    """
    def __init__(self, name: str, observations: Observation = None) -> None:
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

 
    def add_observation(self, value: int, day: int = None) -> Observation:
        """Add observation for a given patient

        :param value: value of measurement of a patient
        :param day: day of measurement of a patient
        """
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(value, day)

        self.observations.append(new_observation)
        return new_observation

class Doctor(Person):
    """A doctor in a clinical trial

    :param name: name of the patient
                 (parameter inherited from class Person)
    :param patients: list of object of the class Patient
                     that are assigned to a given doctor
    :param trials: list of trials that are assigned to a given doctor
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.patients = []
        self.trials = []

    def __str__(self):
        return self.name

    def add_patient(self, patient: Patient) -> None:
        """Add patient object to a list of patients assigned to a given doctor

        :param patient: object of class Patient
        """
        self.patients.append(patient)

    def assign_to_trial(self, trial_name: str) -> None:
        """Assign a given doctor to a trial

        :param trial_name: string with trial name that will be
                           added to trial list assigned to a given doctor
        """
        self.trials.append(trial_name)