from datetime import datetime
import random


class Generator:
    def __init__(self):
        self.names = ['ala', 'ola', 'roman', 'janusz']
        self.locations = ['krakow', 'warszawa', 'kielce']

    @staticmethod
    def _get_random_date():
        return datetime(
            year=2022 + random.randint(0, 2),
            month=random.randint(4, 12),
            day=random.randint(1, 28),
            hour=random.randint(0, 23),
            minute=random.randint(0, 59),
        )

    def generate_data(self, amount):
        all_data = []
        for _ in range(amount):
            temp = []

            temp.append(random.choice(self.names))
            temp.append(str(self._get_random_date()))
            temp.append(str(random.randint(6, 600)))
            temp.append(random.choice(self.locations))
            temp.append(random.choice(self.names))
            temp.append(', '.join(random.choices(self.names, k=random.randint(1, len(self.names)))))

            all_data.append(', '.join(temp) + '\n')

        return all_data

    def save(self, amount):
        with open ('data.txt', 'w') as file:
                data = self.generate_data(amount)
                file.writelines(data)

    @staticmethod
    def load_data(path):
        with open(path, 'r') as file:
            return file.readlines()


# g = Generator()
# # g.save(500)
# print(g.load_data('data.txt))
