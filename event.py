'''The events to be handled'''

class Event:
    def __init__(self, clock, station) -> None:
        self.clock = clock
        self.station = station

class CallInitiationEvent(Event):
    def __init__(self, clock, car_speed, initiation_station,\
                  initiation_position, call_duration, car_direction) -> None:
        super().__init__(clock, initiation_station)

class CallTerminationEvent(Event):
    def __init__(self, clock, terminate_station) -> None:
        super().__init__(clock, terminate_station)

class CallHandoverEvent(Event):
    def __init__(self, clock, car_speed, current_station, remaining_duration, car_direction) -> None:
        super().__init__(clock, current_station)