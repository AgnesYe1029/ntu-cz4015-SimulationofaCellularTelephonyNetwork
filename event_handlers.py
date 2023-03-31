'''The eventhandlers'''

class EventHandler:
    def __init__(self, event_name) -> None:
        self.event_name = event_name

class CallInitiationHandler(EventHandler):
    def __init__(self, event_name) -> None:
        super().__init__(event_name)

class CallTerminationHandler(EventHandler):
    def __init__(self, event_name) -> None:
        super().__init__(event_name)

class CallHandOverHandler(EventHandler):
    def __init__(self, event_name) -> None:
        super().__init__(event_name)
