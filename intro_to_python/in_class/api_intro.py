import requests
import re

from utils.helpers import generate_user_registration_data



session = requests.Session()
session.headers.update({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'})
resp = session.get("https://nop-qa.portnov.com/register")
# name=__RequestVerificationToken type=hidden value=CfDJ8HuVwz9brj1Bh4A0D0tMQOYWcPCyPwcp5byfF1q9JsOeCux1MrQrjHMHX31XWWYwrta7VvGXWjrqAEY34niVYem-skxVazphJvtNMEbVmRrz3MjHKmHToRZB_OgwZSWxZcqBldp-b3XDyDiVI1ENWww
token_value = re.search(r'name=__RequestVerificationToken type=hidden value=(.+?)>', resp.text).group(1)

user = generate_user_registration_data()
payload = {
    'Gender': 'M',
    'FirstName': user.first_name,
    'LastName': user.last_name,
    'DateOfBirthDay': user.birth_date.day,
    'DateOfBirthMonth': user.birth_date.month,
    'DateOfBirthYear': user.birth_date.year,
    'Email': user.email,
    'Company': user.company,
    'Password': user.password,
    'ConfirmPassword': user.password,
    '__RequestVerificationToken': token_value,
    'Newsletter': 'false'
}

print(user.email, user.password)

registration_response = session.post("https://nop-qa.portnov.com/register", data=payload)

pass
