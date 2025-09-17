# Assignment 1: Student Grade Finder
sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 74
sub5 = 88
# Total Marks of five Subjects
Total_Marks = sub1 + sub2 + sub3 + sub4 + sub5
print("Total Marks =", Total_Marks,"/500")

# Percentage of Total Marks
Percentage = (Total_Marks / 500) * 100
print("Percentage =", Percentage,"%")

# Conditions
if Percentage >= 90 and Percentage <=100 :
    print("Grade = A+")
elif Percentage >= 80 and Percentage <= 89 :
    print("Grade = A")
elif Percentage >= 70 and Percentage <= 79 :
    print("Grade = B")
elif Percentage >= 60 and Percentage <= 69 :
    print("Grade = C")
elif Percentage >= 50 and Percentage <= 59 :
    print("Grade = D")
else :
    print("Grade = E")

