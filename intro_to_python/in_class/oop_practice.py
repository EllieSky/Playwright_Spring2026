import time
from datetime import datetime


class Person:
    def __init__(self, full_name, age, gender, occupation=None):
        self.name = full_name
        self.age = age
        self.title = 'Mr.' if gender.lower() == 'male' else 'Ms.'
        self.race = ""
        self.occupation = occupation or 'unemployed'


    def sleep(self):
        if self.age < 18:
            print(f'Sleeping ... {datetime.now()}')
            time.sleep(8)
            print(f'Woke up!!!  {datetime.now()}')
        else:
            for _ in range(5):
                print('Zzzz...')
                time.sleep(1)


    def move(self):
        pass

    def introduction(self):
        print(f'Hi! I am {self.title if self.age >= 18 else ''} {self.name}')



girl = Person("Alice", 5, 'female')

boy = Person("Elon", 11, 'male')

man = Person("Bryan", 29, "male", occupation="Software Developer")

# -------------------

girl.introduction()
man.introduction()
boy.introduction()

print(f'{man.name} is {"a " + man.occupation}')
print(f'{girl.name} is {girl.occupation}')

print(f'\n{girl.name} - go to sleep:')
girl.sleep()

print(f'\n{man.name} - go to sleep:')
man.sleep()


boy.age = 18
boy.introduction()