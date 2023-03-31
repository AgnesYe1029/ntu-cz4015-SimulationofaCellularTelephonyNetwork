"""The events to be handled"""


class Event:
    def __init__(self, time, curr_station) -> None:
        self.time = time
        self.current_station = curr_station


class CallInitiationEvent(Event):
    def __init__(self, time, car_speed, initiation_station,
                 initiation_position, call_duration, car_direction) -> None:
        super().__init__(time, initiation_station)
        self.car_speed = car_speed
        self.initiation_position = initiation_position
        self.call_duration = call_duration
        self.car_direction = car_direction


class CallTerminationEvent(Event):
    def __init__(self, time, terminate_station) -> None:
        super().__init__(time, terminate_station)


class CallHandoverEvent(Event):
    def __init__(self, time, car_speed, current_station, remaining_duration, car_direction) -> None:
        super().__init__(time, current_station)
        self.car_speed = car_speed
        self.remaining_duration = remaining_duration
        self.car_direction = car_direction
