#Ahmed Waqar Qayum Khan
#CIS261
#WK10 VIBE Coding

# =============================================================================
# VIBE CODING DOCUMENTATION
# =============================================================================
# This program was developed using VIBE (Visual Interactive Based Education),
# an AI-powered coding assistant, inside GitHub Codespaces.
#
# INITIAL PROMPT GIVEN TO VIBE:
#   "I need help creating a Python program called Student Grade Calculator.
#    Data: student name, student ID, three test scores (floats), calculated
#    average, and letter grade (A=90-100, B=80-89, C=70-79, D=60-69, F=below 60).
#    Features: add students, auto-calculate average and grade, display all in a
#    formatted table, class statistics, case-insensitive search by name, save to
#    student_grades.txt, load on startup, ESC to exit.
#    Data structure: Option A - list of dictionaries with keys 'name', 'id',
#    'test1', 'test2', 'test3', 'average', 'grade'.
#    File format: pipe-delimited  name|id|test1|test2|test3|average|grade
#    Also use functions, error handling, and 2 decimal places."
#
# DESIGN DECISION I MADE:
#   VIBE offered Option A (list of dictionaries) or Option B (Student class).
#   I chose OPTION A because Week 8 of this course covered dictionaries and
#   file I/O, so this reinforces that material directly.
#
# HOW I REVIEWED AND REFINED VIBE'S OUTPUT:
#   Each refinement below is marked inline with a [VIBE REFINEMENT] comment.
#   1. VIBE's first draft crashed when a user typed letters for a test score.
#      I asked it to add input validation -> get_valid_score()
#   2. VIBE's first draft only exited on menu option 5. The spec also requires
#      the ESC key, so I asked it to accept ESC at the menu prompt too.
#   3. VIBE's first draft divided by zero in the statistics function when no
#      students existed. I added an empty-list guard.
#   4. VIBE originally allowed scores above 100 and below 0. I added range
#      checking since test scores must be 0-100.
#   5. VIBE's original file loader crashed on a malformed line. I asked it to
#      skip bad lines instead of stopping the whole program.
# =============================================================================


# -----------------------------------------------------------------------------
# INPUT FUNCTIONS
# -----------------------------------------------------------------------------

def get_valid_score(prompt):
    """
    Prompts until the user enters a number between 0 and 100.

    [VIBE REFINEMENT #1 and #4]
    VIBE's first draft used a bare float(input(...)) which crashed with a
    ValueError on letter input, and accepted impossible scores like 150.
    I asked VIBE to wrap it in a loop with try/except and range checking.
    """
    while True:
        try:
            score = float(input(prompt))
            if score < 0 or score > 100:
                print("  Score must be between 0 and 100. Please try again.")
                continue
            return score
        except ValueError:
            print("  Invalid entry. Please enter a number.")


def get_student_info():
    """Collects one student's name, ID, and three test scores."""
    print("\n" + "-" * 55)
    print("ADD NEW STUDENT")
    print("-" * 55)
    name = input("Enter student name:  ")
    student_id = input("Enter student ID:  ")
    test1 = get_valid_score("Enter Test 1 score:  ")
    test2 = get_valid_score("Enter Test 2 score:  ")
    test3 = get_valid_score("Enter Test 3 score:  ")
    return name, student_id, test1, test2, test3


# -----------------------------------------------------------------------------
# CALCULATION FUNCTIONS
# -----------------------------------------------------------------------------

def calculate_average(test1, test2, test3):
    """Returns the average of the three test scores."""
    return (test1 + test2 + test3) / 3


def calculate_grade(average):
    """Converts a numeric average into a letter grade."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def calculate_class_statistics(students):
    """
    Returns highest average, lowest average, and class average.

    [VIBE REFINEMENT #3]
    VIBE's first version called max()/min()/sum() directly on an empty list,
    which raised a ValueError and a ZeroDivisionError when no students were
    loaded. I asked it to return zeros when the list is empty instead.
    """
    if len(students) == 0:
        return 0.0, 0.0, 0.0
    averages = [student['average'] for student in students]
    highest = max(averages)
    lowest = min(averages)
    class_average = sum(averages) / len(averages)
    return highest, lowest, class_average


# -----------------------------------------------------------------------------
# DISPLAY FUNCTIONS
# -----------------------------------------------------------------------------

def display_welcome():
    """Prints the program banner and grading scale."""
    print("=" * 55)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 55)
    print("Grading Scale:")
    print("  A = 90-100    B = 80-89    C = 70-79")
    print("  D = 60-69     F = below 60")
    print("=" * 55)


def display_menu():
    """Prints the main menu options."""
    print("\n" + "=" * 55)
    print("MAIN MENU")
    print("=" * 55)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search by Name")
    print("4. View Class Statistics")
    print("5. Save and Exit")
    print("   (or type ESC to save and exit)")
    print("=" * 55)


def display_student_added(name, student_id, average, grade):
    """Confirmation message shown right after a student is added."""
    print("\n" + "=" * 55)
    print("STUDENT ADDED SUCCESSFULLY")
    print("=" * 55)
    print(f"Name:     {name}")
    print(f"ID:       {student_id}")
    print(f"Average:  {average:.2f}")
    print(f"Grade:    {grade}")
    print("=" * 55)


def display_all_students(students):
    """Prints every student in a formatted table."""
    print("\n" + "=" * 75)
    print("ALL STUDENT RECORDS")
    print("=" * 75)
    if len(students) == 0:
        print("No student records found.")
        print("=" * 75)
        return
    print(f"{'Name':<20}{'ID':<10}{'Test1':>8}{'Test2':>8}{'Test3':>8}{'Avg':>9}{'Grade':>7}")
    print("-" * 75)
    for student in students:
        print(f"{student['name']:<20}"
              f"{student['id']:<10}"
              f"{student['test1']:>8.2f}"
              f"{student['test2']:>8.2f}"
              f"{student['test3']:>8.2f}"
              f"{student['average']:>9.2f}"
              f"{student['grade']:>7}")
    print("-" * 75)
    print(f"Total Students: {len(students)}")
    print("=" * 75)


def display_search_results(results, search_name):
    """Prints the records matching a name search, or a not-found message."""
    print("\n" + "=" * 55)
    print(f"SEARCH RESULTS FOR: {search_name}")
    print("=" * 55)
    if len(results) == 0:
        print("No matching student found.")
    else:
        print(f"Found {len(results)} matching record(s):\n")
        for student in results:
            print(f"Name:     {student['name']}")
            print(f"  ID:       {student['id']}")
            print(f"  Test 1:   {student['test1']:.2f}")
            print(f"  Test 2:   {student['test2']:.2f}")
            print(f"  Test 3:   {student['test3']:.2f}")
            print(f"  Average:  {student['average']:.2f}")
            print(f"  Grade:    {student['grade']}")
            print()
    print("=" * 55)


def display_class_statistics(students):
    """Prints highest, lowest, and class average plus a grade distribution."""
    print("\n" + "=" * 55)
    print("CLASS STATISTICS")
    print("=" * 55)
    if len(students) == 0:
        print("No student records to analyze.")
        print("=" * 55)
        return
    highest, lowest, class_average = calculate_class_statistics(students)
    print(f"Total Students:    {len(students)}")
    print(f"Highest Average:   {highest:.2f}")
    print(f"Lowest Average:    {lowest:.2f}")
    print(f"Class Average:     {class_average:.2f}")
    print("-" * 55)
    print("Grade Distribution:")
    for letter in ["A", "B", "C", "D", "F"]:
        count = sum(1 for student in students if student['grade'] == letter)
        print(f"  {letter}: {count}")
    print("=" * 55)


# -----------------------------------------------------------------------------
# SEARCH FUNCTION
# -----------------------------------------------------------------------------

def search_by_name(students, search_name):
    """
    Case-insensitive partial-match search on student name.
    Uses .lower() on both sides so "alice" matches "Alice Johnson".
    """
    results = []
    for student in students:
        if search_name.lower() in student['name'].lower():
            results.append(student)
    return results


# -----------------------------------------------------------------------------
# FILE I/O FUNCTIONS
# -----------------------------------------------------------------------------

def save_students_to_file(students, filename):
    """
    Writes all records to a pipe-delimited file.
    Format: name|id|test1|test2|test3|average|grade
    """
    try:
        with open(filename, 'w') as file:
            for student in students:
                line = (f"{student['name']}|{student['id']}|"
                        f"{student['test1']:.2f}|{student['test2']:.2f}|"
                        f"{student['test3']:.2f}|{student['average']:.2f}|"
                        f"{student['grade']}\n")
                file.write(line)
        print(f"\nSaved {len(students)} student record(s) to {filename}")
    except Exception as e:
        print(f"\nError saving file: {e}")


def load_students_from_file(filename):
    """
    Reads records back into a list of dictionaries.

    [VIBE REFINEMENT #5]
    VIBE's first version let one malformed line crash the whole program.
    I asked it to validate the field count and skip bad lines with a warning
    so a single corrupt row doesn't lose all the other data.
    """
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    if len(parts) != 7:
                        print(f"  Skipping malformed line: {line}")
                        continue
                    student = {
                        'name': parts[0],
                        'id': parts[1],
                        'test1': float(parts[2]),
                        'test2': float(parts[3]),
                        'test3': float(parts[4]),
                        'average': float(parts[5]),
                        'grade': parts[6]
                    }
                    students.append(student)
        print(f"Loaded {len(students)} student record(s) from {filename}")
    except FileNotFoundError:
        print(f"No previous data found in {filename}. Starting fresh.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return students


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------

def main():
    filename = "student_grades.txt"

    display_welcome()

    print("\n--- Loading Previous Data ---")
    students = load_students_from_file(filename)

    while True:
        display_menu()
        choice = input("Enter your choice:  ")

        # [VIBE REFINEMENT #2]
        # VIBE's first draft only exited on option 5. The assignment spec also
        # requires ESC, so I asked it to accept ESC here as well.
        if choice.upper() == "ESC":
            save_students_to_file(students, filename)
            print("\nThank you for using the Student Grade Calculator!")
            print("Goodbye!")
            break

        elif choice == "1":
            name, student_id, test1, test2, test3 = get_student_info()
            average = calculate_average(test1, test2, test3)
            grade = calculate_grade(average)
            student = {
                'name': name,
                'id': student_id,
                'test1': test1,
                'test2': test2,
                'test3': test3,
                'average': average,
                'grade': grade
            }
            students.append(student)
            display_student_added(name, student_id, average, grade)

        elif choice == "2":
            display_all_students(students)

        elif choice == "3":
            search_name = input("\nEnter student name to search:  ")
            results = search_by_name(students, search_name)
            display_search_results(results, search_name)

        elif choice == "4":
            display_class_statistics(students)

        elif choice == "5":
            save_students_to_file(students, filename)
            print("\nThank you for using the Student Grade Calculator!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1-5 or ESC.")


main()