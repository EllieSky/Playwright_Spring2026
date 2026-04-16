import requests, re

from utils.helpers import generate_user_registration_data

session = requests.Session()

resp = session.get("https://nop-qa.portnov.com/register")

#             <input name=__RequestVerificationToken type=hidden value=CfDJ8HuVwz9brj1Bh4A0D0tMQOZ2Mut_kyv8DDvpUfY-GA1tf0RxEXhcDiveuXDTkXlC3RlE3zGk4cKsSfG7maxfuvvYNnIEqyBS_Iqmvvi_Dg42wdrES3IsVD-gDlJ_Ti0fYukG4iq-k05ACaCW8y0VE5c>

#  name=__RequestVerificationToken type=hidden value=(.+?)
token_value = re.search(r'name=__RequestVerificationToken type=hidden value=(.+?)')

user = generate_user_registration_data()

payload = {
    'Gender': user.gender,
    'FirstName': user.first_name,
    'LastName': user.last_name,
    'Email': user.email,
    'Password': user.password,
    'ConfirmPassword': user.password,
    '__RequestVerificationToken': re.search(r'name=__RequestVerificationToken type=hidden value=(.+?)').group(1)
}

pass


