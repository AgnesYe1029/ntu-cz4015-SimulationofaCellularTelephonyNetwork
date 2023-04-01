import numpy as np
from scipy.stats import expon
import random
import system_constants as const


class InputGenerator:
    @staticmethod
    def generate_call_interarrival_time():
        # exponential distribution
        inter_arrival = expon.rvs(const.CALL_INITIATION_DISTRIBUTION_LOC,
                                  const.CALL_INITIATION_DISTRIBUTION_SCALE, 1)[0]
        return inter_arrival

    @staticmethod
    def generate_call_initiation_station():
        # uniform distribution
        return random.randint(0, const.NUM_OF_STATIONS - 1)

    @staticmethod
    def generate_call_duration():
        # exponential distribution
        call_duration = expon.rvs(const.CALL_DURATION_DISTRIBUTION_LOC,
                                  const.CALL_DURATION_DISTRIBUTION_SCALE, size=1)[0]
        return call_duration

    @staticmethod
    def generate_car_speed():
        # normal distribution
        # need to convert from km/h to m/s, dividing by 3.6
        return np.random.normal(const.CAR_SPEED_DISTRIBUTION_LOC,
                                const.CAR_SPEED_DISTRIBUTION_SCALE, size=None)/3.6

    @staticmethod
    def generate_direction():
        # -1: to left, 1: to right
        directions = [-1, 1]
        return random.choice(directions)

    @staticmethod
    def generate_initiation_position_in_cell():
        # this distance is measured from left to right
        return random.uniform(0, const.CELL_DIAMETER)

