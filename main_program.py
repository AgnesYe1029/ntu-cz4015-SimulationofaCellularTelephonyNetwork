
class MainProgram:
    def __init__(self) -> None:
        # clock and time of the last event set to 0
        self.time_of_the_last_event = 0
        self.clock = 0

        # initial event list set to empty
        self.future_event_list = [] 

        # all channels at each station are empty
        self.available_channels = [10] * 20 # an array to denote number of available channels for each cell.

        # system stat counters set to 0
        self.total_number_of_calls = 0
        self.finished_calls = 0
        self.dropped_calls = 0
        self.blocked_calls = 0

    def initiaize():
        # TODO: create the first call initiation event and insert to list.
        pass


    def main_program_routine():
        pass

main = MainProgram()
