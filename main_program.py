from input_generator import InputGenerator
from event import *
from heapq import heappush, heappop


class MainProgram:
    def __init__(self) -> None:
        # clock and time of the last event set to 0
        self.time_of_the_last_event = 0
        self.clock = 0

        # initial event list set to empty
        self.future_event_list = []

        # all channels at each station are empty
        self.available_channels = [10] * 20  # an array to denote number of available channels for each cell.

        # system stat counters set to 0
        self.total_number_of_calls = 0
        self.finished_calls = 0
        self.dropped_calls = 0
        self.blocked_calls = 0

    def initialize(self):
        # TODO: create the first call initiation event and insert to list.
        # generate required RVs
        car_speed = InputGenerator.generate_car_speed()
        initiation_station = InputGenerator.generate_call_initiation_station()
        initiation_position = InputGenerator.generate_initiation_position_in_cell()
        call_duration = InputGenerator.generate_call_duration()
        car_direction = InputGenerator.generate_direction()

        # generate the first call initiation event
        first_call_initiation = CallInitiationEvent(self.clock, car_speed, initiation_station,
                                                    initiation_position, call_duration, car_direction)
        # add the first call init event into FEL
        heappush(self.future_event_list, (self.clock, first_call_initiation))
        print("now the future event list: ", self.future_event_list)

    def main_program_routine(self):
        # simulate 1000 calls
        while self.total_number_of_calls < 1000:
            event = heappop(self.future_event_list)
            self.clock = event.clock  # update the clock
            # TODO: call event handler corresponding to the type of event


main = MainProgram()
main.initialize()
