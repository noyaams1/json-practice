import json


def show_avg_score():
    averages = []
    with open("students.json", "r") as file:
        data = json.load(file)
        for student in data["students"]:
            avg = sum(student["scores"]) / len(student["scores"])
            student["avg"] = avg
            averages.append(avg)
            print(f"Student: {student['name']}, Avg score: {round(avg, 2)}")
    return data, averages


def student_status(data, averages):
    winner = max(averages)
    for student in data["students"]:
        if student["avg"] == winner:
            student["status"] = "Winner"
        else:
            student["status"] = "Participant"
        del student["avg"]

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


new_student = {"name": "Noya", "scores": [8, 12, 9]}


def add_student(new_student, data):
    if any(
        student["name"].casefold() == new_student["name"].casefold()
        for student in data["students"]
    ):
        print(f"The student with the name '{new_student['name']}' already exists.")
        return

    max_id = max((student["id"] for student in data["students"]), default=0)
    new_student["id"] = max_id + 1

    data["students"].append(new_student)

    with open("./students.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Student '{new_student['name']}' added successfully.")


def get_avg(student):
    return sum(student["scores"]) / len(student["scores"])


def print_leaderboard(data):
    print("\n🏆 Leaderboard:")
    print("----------------------------")
    sorted_students = sorted(data["students"], key=get_avg, reverse=True)
    for idx, student in enumerate(sorted_students, 1):
        avg = get_avg(student)
        print(
            f"{idx}. {student['name']} - Avg: {round(avg, 2)} - Status: {student.get('status', 'N/A')}"
        )
    print("----------------------------")


data, averages = show_avg_score()
student_status(data, averages)
add_student(new_student, data)
print_leaderboard(data)
