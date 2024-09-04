student_score = {
    "Harry": 81,
    "Ron": 87,
    "Mark": 99,
    "Jack": 74,
    "Darco": 62,
}


student_greads = {}


for student in student_score:
    score = student_score[student]
    if score > 90:
        student_greads[student] = "Outstanding"

    elif score > 80:
        student_greads[student] = "Exceeds Expectations"

    elif score > 70:
        student_greads[student] = "Aecceptble"

    else:
        student_greads[student] = "Fail"


print(student_greads)
