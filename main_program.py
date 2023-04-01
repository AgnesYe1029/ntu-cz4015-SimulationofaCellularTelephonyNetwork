"""The main program for execution"""

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
        self.dropped_calls = 0
        self.blocked_calls = 0
        self.finished_calls = 0

    def initialize(self):
        # create the first call initiation event and insert to list.
        self.schedule_call_initiation_event(is_first=True)
        print("upon initialization the future event list: ", self.future_event_list)

    def start_simulation(self):
        self.initialize()
        # simulate calls
        while self.finished_calls < 10000:
            event = heappop(self.future_event_list)[1]
            print("======================")
            print("time: ", event.time)
            print("event: ", event)
            print("channel avail: ", self.available_channels)
            self.clock = event.time  # advance the clock
            # event handling corresponding to the type of event
            if isinstance(event, CallInitiationEvent):
                self.handle_call_initiation(event)
            elif isinstance(event, CallHandoverEvent):
                self.handle_call_handover(event)
            elif isinstance(event, CallTerminationEvent):
                self.handle_call_termination(event)
            for x in range(20):
                if self.available_channels[x] < 0:
                    print("channel ", x, "not enough channels")
        print("======================")
        print("num_of_calls: ", self.total_number_of_calls)
        print("blocked_calls: ", self.blocked_calls)
        print("dropped_calls: ", self.dropped_calls)

    def handle_call_initiation(self, event):
        # schedule next call event
        self.schedule_call_initiation_event()

        # process the current call event
        curr_station = event.initiation_station
        if self.available_channels[curr_station] > 0:
            self.available_channels[curr_station] -= 1
            # increment system stats
            self.total_number_of_calls += 1

            time_stay_in_this_cell = (const.CELL_DIAMETER - event.initiation_position) / event.car_speed \
                if event.car_direction == 1 else event.initiation_position / event.car_speed

            if event.call_duration <= time_stay_in_this_cell:  # if call ended before leaving this station
                self.schedule_termination_event(self.clock + event.call_duration, curr_station)
            else:  # the call ends after leaving the station, handover needed
                next_station = curr_station + event.car_direction
                if next_station < 0 or next_station > 19:
                    # the car is passing the ends of the highway
                    self.schedule_termination_event(self.clock + time_stay_in_this_cell, curr_station)
                else:
                    next_station = curr_station + event.car_direction
                    remaining_call_duration = event.call_duration - time_stay_in_this_cell
                    # schedule call_handover
                    self.schedule_call_handover_event(self.clock + time_stay_in_this_cell,
                                                      event.car_speed, curr_station,
                                                      next_station, remaining_call_duration, event.car_direction)
        else:  # this call is blocked
            self.blocked_calls += 1
            self.finished_calls += 1

        self.time_of_the_last_event = event.time

    def handle_call_termination(self, event):
        # release the channel
        self.available_channels[event.terminate_station] += 1

        # update system stats
        self.time_of_the_last_event = event.time
        self.finished_calls += 1

    def handle_call_handover(self, event):
        # release the previous channel used
        prev_station = event.prev_station
        curr_station = event.next_station
        self.available_channels[prev_station] += 1

        if self.available_channels[curr_station] > 0:
            self.available_channels[curr_station] -= 1
            time_stay_in_this_cell = const.CELL_DIAMETER / event.car_speed

            if time_stay_in_this_cell > event.remaining_duration:
                # the call ended before leaving this cell
                self.schedule_termination_event(self.clock + event.remaining_duration, curr_station)
            else:
                # calculate the next station
                next_station = curr_station + event.car_direction
                if next_station < 0 or next_station > 19:
                    # across the ends of the highway, call terminated
                    self.schedule_termination_event(self.clock + time_stay_in_this_cell, curr_station)
                else:
                    remaining_duration = event.remaining_duration - time_stay_in_this_cell
                    self.schedule_call_handover_event(self.clock + time_stay_in_this_cell,
                                                      event.car_speed, curr_station, next_station,
                                                      remaining_duration, event.car_direction)
        else:
            # the call is dropped
            self.dropped_calls += 1
            self.finished_calls += 1

        self.time_of_the_last_event = event.time

    def schedule_termination_event(self, term_time, term_station):
        heappush(self.future_event_list, (term_time, CallTerminationEvent(term_time, term_station)))

    def schedule_call_handover_event(self, handover_time, car_speed, prev_station, next_station,
                                     remaining_duration, car_direction):
        heappush(self.future_event_list,
                 (handover_time, CallHandoverEvent(handover_time, car_speed, prev_station,
                                                   next_station, remaining_duration, car_direction)))

    def schedule_call_initiation_event(self, is_first=False):
        # generate call init event
        next_call_init_time = self.clock + InputGenerator.generate_call_interarrival_time()
        next_car_speed = InputGenerator.generate_car_speed()
        next_call_init_station = InputGenerator.generate_call_initiation_station()
        next_call_init_position = InputGenerator.generate_initiation_position_in_cell()
        next_call_duration = InputGenerator.generate_call_duration()
        next_car_direction = InputGenerator.generate_direction()
        next_call_init_event = CallInitiationEvent(next_call_init_time, next_car_speed, next_call_init_station,
                                                   next_call_init_position, next_call_duration, next_car_direction)
        if is_first:
            self.clock = next_call_init_event
        heappush(self.future_event_list, (next_call_init_time, next_call_init_event))


if __name__ == "__main__":
    main = MainProgram()
    main.start_simulation()
