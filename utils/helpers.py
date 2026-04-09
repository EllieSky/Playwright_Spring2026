#helper we can call on to retrieve data
#Convient  user friendly way to transmit data
#import
import datetime
from dataclasses import dataclass
from faker import Faker

#Way to pass data easy to use
@dataclass
class RegisterUserData:
    first_name: str
    last_name: str
    birth_date: datetime.date
    email: str
    company: str
    password: str




def generate_user_registration_data():

    f = Faker()

    return RegisterUserData (
        first_name = f.first_name_female(),
        last_name= f.last_name(),
        birth_date = f.date_of_birth(),
        email = f.free_email(),
        company = f.company(),
        password = f.password(8)

    )

