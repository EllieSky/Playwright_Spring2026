person = ""
weather = "sunny"

if weather == "rain":
    person += "Boots"
else:
    person += "sneakers"

# print(person)


speed = 60
traffic_light = "strawberry"

if traffic_light == "red":
    speed = 0
elif traffic_light == "green":
    pass
elif traffic_light == "yellow":
    speed += 10
# else:
#     speed = 0
#     print("Aliens are taking over!!!!!")

if traffic_light in {"red", "green", "yellow"}:
    print("Speed is: ", speed)


special_parking = False
person_type = "abled"
has_card = False

if ((person_type == "disabled" and has_card)
        or person_type == "veteran"
        or person_type == "pregnant"):
    special_parking = True

if special_parking:
    "You get special parking!!!"
else:
    "Please park in regular spot."