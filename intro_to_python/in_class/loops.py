# for bottles in range(10, 0, -1):
#     ending = "s" if bottles > 1 else ""
#
#     # if bottles > 1:
#     #     ending = "s"
#     # else:
#     #     ending = ""
#
#     print(f"{bottles} bottle{ending} of juice on the wall")
#     print(f"{bottles} bottle{ending} of juice...")
#     print("you take one down, pass it around")
#     bottles -= 1
#     if bottles == 1:
#         print(f"{bottles} bottle of juice on the wall")
#     else:
#         print(f"{bottles} bottles of juice on the wall")
#
#     # print(f"{bottles} bottles of juice on the wall") if bottles > 0 else print(f"{bottles} bottle of juice on the wall")
#
#     print("..........")
#
# students = [
#     {'name': 'Alice', 'score': 85},
#     {'name': 'Bob', 'score': 92},
#     {'name': 'Carol', 'score': 78}
# ]
#
# student_name :str = ""
# high_score = 0
# for student in students:
#     if student['score'] > high_score:
#         high_score = student['score']
#         student_name = student['name']
# print(f"{student_name} has a high score of {high_score}")
#
#
# students2 = {
#     'Alice': 85,
#     'Bob': 92,
#     'Carol': 78
# }
#
# student_high_score :tuple = ("", 0)
# for name, score in students2.items():
#     if score > student_high_score[1]:
#         student_high_score = name, score
# print(f"{student_high_score[0]} has a high score of {student_high_score[1]}")


num_list = [11, 1, 22, 9, 3, 11, 4, 6, 11, 8, 9]
# for i, num in enumerate(num_list):
#     for j in range(i + 1, len(num_list)):
#         if num_list[j] == num:
#             print(f"{num} has at least 1 duplicate")
#         # else:
#         #     continue


result = {}
for num in num_list:
    if num not in result:
        result.setdefault(num, 1)
    else:
        result[num] += 1

for key, value in result.items():
    if value > 1:
        print(f"{key} has {value} duplicates")


# Challenge - Reverse WORDS in a sentence
# Example: "I love walking my dog"  -> "dog my walking love I"

sentence = "I love walking my dog"
sentence = " ".join(sentence.split()[::-1])
print(sentence)

# is_true = True

def do_while_loop():
    counter = 0
    while True:
        counter += 1
        if counter % 2:
            print(f'Going to skip input now. Counter: {counter}')
            continue
        print("Running loop #" + str(counter))
        stop = input("Should I stop now? Y/N")
        if stop.upper() == "Y":
            break
    print("Good bye!  :)")

do_while_loop()


