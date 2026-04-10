

def get_full_name(first_name, last_name, middle_name=""):
    return  first_name + " " + middle_name + " " + last_name
    # return f"{first_name} {middle_name} {last_name}"
    # return " ".join((first_name, middle_name, last_name))

def get_health_data(age, weight=None, height=None):
    if not height:    # Checks for NOT zero, empty space, None, []/{}
        height = 0      # if height is "falsy" it assigns int 0

    if age and int(age) >= 18:
        return "Adult", weight, "tall" if int(height) > 72 else "short"
    return "Child", weight, "small" if int(height) < 48 else "bigger"



# full_name = get_full_name(
#     first_name=input("Enter your first name: "),
#     last_name=input("Enter your last name: "),
# )
#
# print(full_name)


print(get_health_data("18"))   # Adult, None, short
print(get_health_data(None))    # Child, None, small
print(get_health_data(18))      # Adult, None, short
print(get_health_data(60, height=75))   # Adult, None, tall
print(get_health_data(14, 120, 49)) # child, 120, bigger
print(get_health_data(18, height=47, weight=100))  # Adult, 100, short
