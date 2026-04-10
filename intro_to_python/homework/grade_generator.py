def calculate_grade(score):
    # Step 1: Handle invalid input
    if score < 0 or score > 100:
        print(f"Score {score} is invalid. Please enter a value between 0 and 100.")
        return

    # Step 2: Determine Letter Grade and Modifier
    if score >= 90:
        grade = "A"
        if score < 93:
            grade += "-"
    elif score >= 80:
        grade = "B"
        if score >= 87:
            grade += "+"
        elif score < 83:
            grade += "-"
    elif score >= 70:
        grade = "C"
        if score >= 77:
            grade += "+"
        elif score < 73:
            grade += "-"
    elif score >= 60:
        grade = "D"
        if score >= 67:
            grade += "+"
        elif score < 63:
            grade += "-"
    else:
        grade = "F"

    print(f"Score: {score} -> Grade: {grade}")

# Test Cases
test_scores = [95, 89, 82, 76, 65, 55]

for s in test_scores:
    calculate_grade(s)
