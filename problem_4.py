import json

def best(students):
    return max(students, key=lambda x: x["grade"])

def worst(students):
    return min(students, key=lambda x: x["grade"])

def average(students):
    return sum(x["grade"] for x in students) / len(students)


with open("students.json", encoding="utf-8") as f:
    students = json.load(f)

best_student = best(students)
worst_student = worst(students)
avg = average(students)

print(students)

print(f"Eng yaxshi talaba: {best_student['name']} — {best_student['grade']}")
print(f"Eng past baho: {worst_student['name']} — {worst_student['grade']}")
print(f"O'rtacha baho: {avg}")