"""The events to be handled"""


class Event:
    def __init__(self, time) -> None:
        self.time = time


class CallInitiationEvent(Event):
    def __init__(self, time, car_speed, initiation_station,
                 initiation_position, call_duration, car_direction) -> None:
        super().__init__(time)
        self.initiation_station = initiation_station
        self.car_speed = car_speed
        self.initiation_position = initiation_position
        self.call_duration = call_duration
        self.car_direction = car_direction


class CallTerminationEvent(Event):
    def __init__(self, time, terminate_station) -> None:
        super().__init__(time)
        self.terminate_station = terminate_station


class CallHandoverEvent(Event):
    def __init__(self, time, car_speed, prev_station, next_station, remaining_duration, car_direction) -> None:
        super().__init__(time)
        self.car_speed = car_speed
        self.prev_station = prev_station
        self.next_station = next_station
        self.remaining_duration = remaining_duration
        self.car_direction = car_direction
