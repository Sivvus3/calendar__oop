from datetime import datetime, timedelta


class Event:
    def __init__(self, name, start_date, duration, location, owner, participants=tuple()):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.location = location
        self.owner = owner
        self.participants = participants

    def end_of_meeting(self):
        return self.start_date + timedelta(minutes=self.duration)

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if value == '':
            raise ValueError(f'Location can`t be empty')
        self._location = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError(f'Name can`t be empty')
        self._name = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if value <= 5:
            raise ValueError(f'Duration: {value} is too short. Should have more than 5 minutes')
        self._duration = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, dt):
        if dt < datetime.now() + timedelta(minutes=15):
            raise ValueError(f'Date {dt} is less than 15 minutes from now')
        self._start_date = dt

    def __str__(self):
        return f'{type(self).__name__}: {self.name}'

    def __repr__(self):
        attrs = ", ".join([f"{k[1:] if k[0] == '_' else k}={repr(v)}" for k, v in self.__dict__.items()])
        return f"{type(self).__name__}({attrs})"
