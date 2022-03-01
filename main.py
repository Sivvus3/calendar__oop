import os
from datetime import datetime

from data_generator.generator import Generator
from event import Workshop, Meeting, Event
from planner import Planner


def main():
    data = Generator.load_data(os.path.join('data_generator', 'data.txt'))
    event_list = []

    for item in data:
        element_list = []
        participant_list = []
        for idx, element in enumerate(item.split(', ')):
            if element.isdigit():
                element_list.append(int(element))
                continue

            try:
                dt = datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
                element_list.append(dt)
                continue
            except Exception as err:
                pass

            if idx >= 5:
                participant_list.append(element)
                continue

            element_list.append(element)

        element_list.append(participant_list)
        event_list.append(Event(*element_list))

    planner = Planner(event_list)
    print(repr(planner))


if __name__ == '__main__':
    main()