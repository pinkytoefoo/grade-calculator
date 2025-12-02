import os
import matplotlib.pyplot as plt

menu_options = """1. Student grade
2. Assignment statistics
3. Assignment graph
"""

"""
FILE LAYOUTS
- SID = student id (3 ints)
- AID = assignment id (5 ints)

students.txt
<SID>First Last

assignments.txt
Assignment Name
AID
Points worth

submissions/<hash>.txt
<SID>|<AID>|<GRADE>
"""

def parse_submission(data: str):
    return tuple(data.split("|"))

def main():
    print(menu_options)
    option = input("Enter your selection: ")

    # ------------ OPTION 1 ------------
    if option == "1":
        student_name = str(input("What is the student's name: "))
        final_grade: int = 0
        assignments = 0
        student_id = None
        with open("data/students.txt", "r") as f:
            for line in f.readlines():
                # remove whitespace for accurate comparison checks
                if line[3:].strip() == student_name.strip():
                    student_id = line[:3]
                    # print(student_id)
        
        for filename in os.listdir("data/submissions"):
            with open(f"data/submissions/{filename}", "r") as f:
                data = f.read().strip()
                # ignore assignment id
                sid, _, grade = parse_submission(data)
                if sid == student_id:
                    final_grade += int(grade)
                    assignments += 1
        
        if final_grade != 0:
            final_grade = int(final_grade / assignments)
            print(f"{final_grade}%")
            return
        
        print("Student not found")


    # ------------ OPTION 2 ------------
    if option == "2":
        assignment_name = str(input("What is the assignment name: "))
        assignment_id = None
        with open("data/assignments.txt", "r") as f:
            data = f.read().splitlines()
            # only check assignmnet name lines
            for i, name in enumerate(data):
                if i % 3 == 0 and name == assignment_name:
                    # go one line down to get assignment id
                    assignment_id = data[i+1]
                    # print(assignment_id)
        
        # set min to 100 so that we only go lower and max at 0 so we only go higher
        grades_stats = {"Min": 100, "Max": 0, "Avg": 0}
        avg = 0
        count = 0
        for filename in os.listdir("data/submissions"):
            with open(f"data/submissions/{filename}", "r") as f:
                data = f.read().strip()
                _, aid, grade = parse_submission(data)
                if aid == assignment_id:
                    grade = int(grade)
                    
                    if grade < grades_stats["Min"]:
                        grades_stats["Min"] = grade
                    if grade > grades_stats["Max"]:
                        grades_stats["Max"] = grade
                    
                    avg += grade
                    count += 1

        if count != 0 :
            avg = int(avg/count)
            grades_stats["Avg"] = avg
            for stat in grades_stats:
                print(f"{stat}: {grades_stats[stat]}%")
            return
        
        # better to print this earlier to avoid doing extra logic but this works for now
        print("Assignment not found")


    # ------------ OPTION 3 ------------
    if option == "3":
        assignment_name = str(input("What is the assignment name: "))
        assignment_id = None
        with open("data/assignments.txt", "r") as f:
            data = f.read().splitlines()
            # only check assignmnet name lines
            for i, name in enumerate(data):
                if i % 3 == 0 and name == assignment_name:
                    # go one line down to get assignment id
                    assignment_id = data[i+1]
        
        if assignment_id == None:
            print("Assignment not found")
            return
        
        scores = []
        for filename in os.listdir("data/submissions"):
            with open(f"data/submissions/{filename}", "r") as f:
                data = f.read().strip()
                _, aid, grade = parse_submission(data)
                if aid == assignment_id:
                    scores.append(int(grade))
        
        plt.hist(scores, bins=[50,55,60,65,70,75,80,85,90,95,100])
        plt.show()


if __name__ == "__main__":
    main()