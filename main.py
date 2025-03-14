students = []

def get_student_data():
    student = {}
    student["name"] = input("Enter Student Name: ")
    student["roll_no"] = input("Enter Roll Number: ")

    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    student["marks"] = marks
    students.append(student)
    print(f"Record of {student['name']} inserted successfully!")

def calculate_grade(marks):
    total = sum(marks.values())
    percentage = (total / 500) * 100
    
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "F"
    else:
        grade = "Fail"
    
    return total, percentage, grade



def generate_report_card():
    print("\n======= Student Report Cards =======\n")
    for student in students:
        total, percentage, grade = calculate_grade(student["marks"])
        
        print(f"Student Name: {student['name']}")
        print(f"Roll Number: {student['roll_no']}")
        print("Marks:")
        
        for subject, mark in student["marks"].items():
            print(f"  {subject}: {mark}")

        print(f"Total Marks: {total}/500")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print("-" * 30)

while True:
    get_student_data()
    choice = input("Do you want to insert more? (Y/N): ").strip().lower()
    
    if choice == 'n':
        break

generate_report_card()