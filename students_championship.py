import json


# calculating and printing the average score for each student
def show_avg_score():
    averages = []  # to store average scores
    with open("students.json", "r") as file:
        data = json.load(file)
        for student in data["students"]:
            avg = sum(student["scores"]) / len(student["scores"])
            student["avg"] = avg  # storing the average for later use
            averages.append(avg)
            print(f"Student: {student['name']}, Avg score: {round(avg, 2)}")
    return data, averages


# determining student status: Winner or Participan
def student_status(data, averages):
    winner = max(averages)
    for student in data["students"]:
        if student["avg"] == winner:
            student["status"] = "Winner"
        else:
            student["status"] = "Participant"
        del student["avg"]  # cleaning up temporary avg field

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)  # Saving updated data with statuses


new_student = {"name": "Noya", "scores": [8, 12, 9]}


# adding new student & updating data
def add_student(new_student, data):
    # checking if a student with the same name already exists
    if any(
        student["name"].casefold() == new_student["name"].casefold()
        for student in data["students"]
    ):
        print(f"The student with the name '{new_student['name']}' already exists.")
        return
    # assigning a new unique ID based on the highest existing one
    max_id = max((student["id"] for student in data["students"]), default=0)
    new_student["id"] = max_id + 1

    data["students"].append(new_student)

    with open("./students.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Student '{new_student['name']}' added successfully.")


# function to get average score for a student for leaderboard function
def get_avg(student):
    return sum(student["scores"]) / len(student["scores"])


def print_leaderboard(data):
    print("\n🏆 Leaderboard:")
    print("----------------------------")
    # sorting students from highest to lowest average score
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
