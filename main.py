# Built-in imports
import math

# Your code below
GRADE = {}
for score in range(0, 101):
    if score >= 70:
        GRADE[score] = "A"
    elif score >= 60:
        GRADE[score] = "B"
    elif score >= 55:
        GRADE[score] = "C"
    elif score >= 50:
        GRADE[score] = "D"
    elif score >= 45:
        GRADE[score] = "E"
    elif score >= 40:
        GRADE[score] = "S"
    elif score < 40:
        GRADE[score] = "U"

def read_testscores(filename):
    testscores = []
    with open(filename, "r") as f:
        header = f.readline().strip().split(",")

        for line in f:
            line = line.strip().split(",")
            p1, p2, p3, p4 = int(line[2]), int(line[3]), int(line[4]), int(line[5])
            quadruple = (p1, p2, p3, p4)
            overall = math.ceil((p1/30 * 15) + (p2/40 * 30) + (p3/80 * 35) + (p4/30 * 20))
            score_dict = {"class": line[0], "name": line[1], "overall": overall, "grade": GRADE.get(overall)}
            testscores.append(score_dict)

    return testscores

def analyze_grades(studentdata):
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "S": 0, "U": 0}
    grades_by_class = {"Class1": None, 
                       "Class2": None,
                       "Class3": None,
                        "Class4": None, 
                        "Class5": None,
                        "Class6": None,
                        "Class7": None, 
                        "Class8": None,
                        "Class9": None,
                        "Class10": None, 
                        "Class11": None,
                        "Class12": None,
                        "Class13": None, 
                        "Class14": None,
                        "Class15": None,
                        "Class16": None, 
                        "Class17": None,
                        "Class18": None,}
    what_class = studentdata[0]["class"]
    for i in studentdata:
        if i.get("class") == what_class:
            what_grade = i.get("grade")
            if what_grade == "A":
                grade_count["A"] += 1
            elif what_grade == "B":
                grade_count["B"] += 1
            elif what_grade == "C":
                grade_count["C"] += 1
            elif what_grade == "D":
                grade_count["D"] += 1
            elif what_grade == "E":
                grade_count["E"] += 1
            elif what_grade == "S":
                grade_count["S"] += 1
            elif what_grade == "U":
                grade_count["U"] += 1
            grades_by_class.update({what_class: grade_count})

        else:
            grade_count = {x: 0 for x in grade_count}
            what_class = i.get("class")
            what_grade = i.get("grade")
            if what_grade == "A":
                grade_count["A"] += 1
            elif what_grade == "B":
                grade_count["B"] += 1
            elif what_grade == "C":
                grade_count["C"] += 1
            elif what_grade == "D":
                grade_count["D"] += 1
            elif what_grade == "E":
                grade_count["E"] += 1
            elif what_grade == "S":
                grade_count["S"] += 1
            elif what_grade == "U":
                grade_count["U"] += 1
            grades_by_class.update({what_class: grade_count})

    return grades_by_class





