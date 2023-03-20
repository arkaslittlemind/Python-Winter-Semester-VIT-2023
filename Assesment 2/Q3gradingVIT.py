subject=input("Enter the subject: ")

student_marks = float(input("Enter the marks secured by the student: "))

class_average = float(input("Enter the class average: "))

deviation = student_marks - class_average

if (deviation >= 20):
    print("Grade in",subject,": S")

elif (deviation >= 10):
    print("Grade in",subject,": A")

elif (-5 <= deviation <= 5):
    print("Grade in",subject,": B")

elif (deviation <= -10):
    print("Grade in",subject,": C")

elif (deviation <= -15):
    print("Grade in",subject,": D")

else:
    print("Grade in",subject,": F")