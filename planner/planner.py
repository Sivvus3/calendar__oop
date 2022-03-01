class Planner:
    def __init__(self, events):
        self.events = events

    def __str__(self):
        return f'{type(self).__name__}: {self.events}'

    def __repr__(self):
        attrs = ", ".join([f"{k[1:] if k[0] == '_' else k}={repr(v)}" for k, v in self.__dict__.items()])
        return f"{type(self).__name__}({attrs})"
