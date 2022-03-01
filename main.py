from datetime import datetime
from event import Workshop, Meeting, Event
from planner import Planner


def main():
    e = Event('python', datetime.strptime('01-03-2022 16:19', '%d-%m-%Y %H:%M'), 60, 'better world', 'pawel',
              ('michal', 'marcin', 'renata'))
    w = Workshop('python', datetime.strptime('01-03-2022 16:19', '%d-%m-%Y %H:%M'), 60, 'better world',
                 'pawel', ['michal', 'marcin', 'renata'], 'online')
    m = Meeting('ala ma ejc', datetime.strptime('01-03-2022 16:19', '%d-%m-%Y %H:%M'), 60, 'better world',
                'pawel', ['michal', 'marcin', 'renata'], 'arctovsky')
    e.start_date = datetime.strptime('01-03-2022 16:19', '%d-%m-%Y %H:%M')

    print(w.duration)
    print(w.start_date)
    print(w.end_of_meeting())
    print(w.end_of_meeting() - e.start_date)
    # print(repr(e))
    # print(repr(w))
    # print(repr(m))
    # check_dt = e.check_date(datetime.strptime('01-03-2022 16:19', '%d-%m-%Y %H:%M'))
    # print(check_dt)

    # planner = Planner([])
    # print(repr(planner))


if __name__ == '__main__':
    main()
