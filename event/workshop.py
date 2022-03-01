from datetime import timedelta

from event import Event


class Workshop(Event):
    def __init__(self, name, start_date, duration, location, owner, participants, kind='stationary'):
        super().__init__(name, start_date, duration, location, owner, participants)
        self.kind = kind

        def end_of_meeting(self):
            dt = super().end_of_meeting()
            return dt + timedelta(minutes=10)
