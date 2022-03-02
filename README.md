# Inflam
![Continuous Integration build in GitHub Actions](https://github.com/SamuelHLewis/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features
Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites
Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Instructions
In order to build the repo as a package, type the following command on the home directory of this repo:
`pip install . -e` 

## Walkthrough

To run this software, you need to execute the `inflamation-analysis.py` file as:
`python3 /<your_location>/python-intermediate-inflammation/inflammation-analysis.py`

There are some parameters that needed to be specifed, while others are optional:

```
infiles: The file containing the infmamation data to be displayed
view: Optional [default: visualize] - which view should be used. Select either visualize or record.
patient: Optional [default: 0] - which patient from the list should be displayed
```

If tests needed to be run, these are located on the `tests` folder and they can be run suing the command `pytest tests/test_models.py` 

## Conntact
In case you identify a bug/misbehaviour of this software, please either create a new issue or contact leonidas.souliotis at astrazeneca.com