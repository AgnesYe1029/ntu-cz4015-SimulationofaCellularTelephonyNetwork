import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as ss
from scipy.stats import expon
import random
import system_constants as const

class InputGenerator:
    @staticmethod
    def generate_call_initiation_time():
        # exponential distribution
        interrarrival = expon.rvs(const.CALL_INITIATION_DISTRIBUTION_LOC, \
                                             const.CALL_INITIATION_DISTRIBUTION_SCALE, 1)[0]
        return interrarrival

    @staticmethod
    def generate_call_initiation_location():
        # uniform distribution
        return random.randint(0, const.NUM_OF_STATIONS-1)
    
    @staticmethod
    def generate_call_duration():
        # exponential distribution
        call_duration = expon.rvs(const.CALL_DURATION_DISTRIBUTION_LOC, const.CALL_DURATION_DISTRIBUTION_SCALE, size=1)[0]
        return call_duration
    
    @staticmethod
    def generate_car_speed():
        # normal distribution
        return np.random.normal(const.CAR_SPEED_DISTRIBUTION_LOC, const.CAR_SPEED_DISTRIBUTION_SCALE, size=None)

    @staticmethod
    def generate_direction():
        directions = [-1, 1]
        return random.choice(directions)


    @staticmethod
    def generate_initiation_position_in_cell():
        # this distance is measured from left to right
        return random.uniform(0, const.CELL_DIAMETER)
