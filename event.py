class Event:
    def __init__(self, name, start_date, duration, location, owner, participants,):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.location = location
        self.owner = owner
        self.participants = participants

    def __str__(self):
        return f'{type(self).__name__}: {self.name}'


    def __repr__(self):
        attrs = ", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])
        return f"{type(self).__name__}({attrs})"


class Workshop(Event):
    def __init__(self, name, start_date, duration, location, owner, participants, kind='stationary'):
        super().__init__(name, start_date, duration, location, owner, participants)
        self.kind = kind


class Meeting(Event):
    def __init__(self, name, start_date, duration, location, owner, participants, room):
        super().__init__(name, start_date, duration, location, owner, participants)
        self.room = room




e = Event('python', '28-02-2022', 60, 'better world', 'pawel', ['michal', 'marcin', 'renata'])
w = Workshop('python', '28-02-2022', 60, 'better world', 'pawel', ['michal', 'marcin', 'renata'], 'online')
m = Meeting('python', '28-02-2022', 60, 'better world', 'pawel', ['michal', 'marcin', 'renata'], 'arctovsky')

print(repr(e))
print(repr(w))
print(repr(m))



