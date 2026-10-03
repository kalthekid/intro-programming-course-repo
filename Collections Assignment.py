def determineLetterGrade(average):
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

studentName = input("Enter student name: ")

grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

gradesList = [grade1, grade2, grade3, grade4, grade5]

averageScore = (grade1 + grade2 + grade3 +grade4 +grade5) / len(gradesList)

letterGrade = determineLetterGrade(averageScore)

print()
print(studentName)
print("Average:", averageScore)
print("Letter Grade:", letterGrade)