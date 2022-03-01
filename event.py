from datetime import datetime, timedelta


class Event:
    def __init__(self, name, start_date, duration, location, owner, participants=tuple()):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.location = location
        self.owner = owner
        self.participants = participants

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


class Workshop(Event):
    def __init__(self, name, start_date, duration, location, owner, participants, kind='stationary'):
        super().__init__(name, start_date, duration, location, owner, participants)
        self.kind = kind


class Meeting(Event):
    def __init__(self, name, start_date, duration, location, owner, participants, room):
        super().__init__(name, start_date, duration, location, owner, participants)
        self.room = room


e = Event('python', datetime.strptime('01-03-2022 16:19', '%d-%m-%Y %H:%M'), 6, 'better world', 'pawel',
          ('michal', 'marcin', 'renata'))
# w = Workshop('python', '28-02-2022', 60, 'better world', 'pawel', ['michal', 'marcin', 'renata'], 'online')
# m = Meeting('ala ma ejc', '28-02-2022', 60, 'better world', 'pawel', ['michal', 'marcin', 'renata'], 'arctovsky')
e.start_date = datetime.strptime('01-04-2022 16:19', '%d-%m-%Y %H:%M')
print(repr(e))

# print(repr(e))
# print(repr(w))
# print(repr(m))
# check_dt = e.check_date(datetime.strptime('01-03-2022 16:19', '%d-%m-%Y %H:%M'))
# print(check_dt)


class Planner:
    def __init__(self, events):
        self.events = events

    def __str__(self):
        return f'{type(self).__name__}: {self.events}'

    def __repr__(self):
        attrs = ", ".join([f"{k[1:] if k[0] == '_' else k}={repr(v)}" for k, v in self.__dict__.items()])
        return f"{type(self).__name__}({attrs})"


planner = Planner([])
print(repr(planner))