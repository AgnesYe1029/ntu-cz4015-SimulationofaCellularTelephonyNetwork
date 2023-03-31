"""The events to be handled"""


class Event:
    def __init__(self, clock, station) -> None:
        self.clock = clock
        self.station = station


class CallInitiationEvent(Event):
    def __init__(self, clock, car_speed, initiation_station,
                 initiation_position, call_duration, car_direction) -> None:
        super().__init__(clock, initiation_station)
        self.car_speed = car_speed
        self.initiation_position = initiation_position
        self.call_duration = call_duration
        self.car_direction = car_direction


class CallTerminationEvent(Event):
    def __init__(self, clock, terminate_station) -> None:
        super().__init__(clock, terminate_station)


class CallHandoverEvent(Event):
    def __init__(self, clock, car_speed, current_station, remaining_duration, car_direction) -> None:
        super().__init__(clock, current_station)
        self.car_speed = car_speed
        self.remaining_duration = remaining_duration
        self.car_direction = car_direction
