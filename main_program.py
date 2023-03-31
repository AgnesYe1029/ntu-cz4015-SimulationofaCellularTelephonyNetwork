from input_generator import InputGenerator
from event import *
from heapq import heappush, heappop
import system_constants as const


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
        call_init_time = self.clock + InputGenerator.generate_call_interarrival_time()
        car_speed = InputGenerator.generate_car_speed()
        initiation_station = InputGenerator.generate_call_initiation_station()
        initiation_position = InputGenerator.generate_initiation_position_in_cell()
        call_duration = InputGenerator.generate_call_duration()
        car_direction = InputGenerator.generate_direction()

        # generate the first call initiation event
        first_call_initiation = CallInitiationEvent(call_init_time, car_speed, initiation_station,
                                                    initiation_position, call_duration, car_direction)
        # add the first call init event into FEL
        heappush(self.future_event_list, (first_call_initiation.time, first_call_initiation))
        print("now the future event list: ", self.future_event_list)

    def main_program_routine(self):
        # simulate 1000 calls
        while self.total_number_of_calls < 1000:
            event = heappop(self.future_event_list)
            self.clock = event.time  # update the clock
            # event handling corresponding to the type of event
            if isinstance(event, CallInitiationEvent):
                self.handle_call_initiation(event)
            elif isinstance(event, CallHandoverEvent):
                self.handle_call_handover(event)
            elif isinstance(event, CallTerminationEvent):
                self.handle_call_termination(event)

    def handle_call_initiation(self, event):
        # schedule next call event
        next_call_init_time = self.clock + InputGenerator.generate_call_interarrival_time()
        next_car_speed = InputGenerator.generate_car_speed()
        next_call_init_station = InputGenerator.generate_call_initiation_station()
        next_call_init_position = InputGenerator.generate_initiation_position_in_cell()
        next_call_duration = InputGenerator.generate_call_duration()
        next_car_direction = InputGenerator.generate_direction()
        next_call_init_event = CallInitiationEvent(next_call_init_time, next_car_speed, next_call_init_station,
                                                   next_call_init_position, next_call_duration, next_car_direction)

        # process the current call event
        curr_station = event.current_station
        if self.available_channels[curr_station] > 0:
            self.available_channels[curr_station] -= 1

            # increment system stats
            self.total_number_of_calls += 1

            time_stay_in_this_cell = (const.CELL_DIAMETER - event.initiation_position)/event.car_direction \
                if event.car_direction == 1 else event.initiation_position/event.car_direction

            if event.call_duration <= time_stay_in_this_cell:  # if call ended before leaving this station
                self.schedule_termination_event(self.clock + event.call_duration, curr_station)
            else:  # the call ends after leaving the station, handover needed
                leaving_cell_time = self.clock + time_stay_in_this_cell
                if curr_station + event.car_direction == -1 or curr_station + event.car_direction == 20:
                    # the car is passing the ends of the highway
                    self.schedule_termination_event(leaving_cell_time, curr_station)
                else:
                    next_station = curr_station + event.car_direction
                    remaining_call_duration = event.call_duration - time_stay_in_this_cell
                    # TODO: schedule call_handover

    def handle_call_termination(self, event):
        # release the channel
        self.available_channels[event.current_station] += 1

        # update system stats
        self.finished_calls += 1
        self.time_of_the_last_event = event.time

    def handle_call_handover(self, event):
        pass

    def schedule_termination_event(self, term_time, term_station):
        heappush(self.future_event_list, CallTerminationEvent(term_time, term_station))

    def schedule_call_handover_event(self, handover_time, car_speed, next_station, remaining_duration, car_direction):
        pass


main = MainProgram()
main.initialize()
