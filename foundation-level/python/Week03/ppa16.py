"""
Multiple Select Questions (MSQ) could have more than one correct answers. The marks scored by a student in a MSQ will be determined by the following conditions:
(1) If the question has c correct options, each individual correct option carries c/n marks.
(2) If a student selects any of the wrong options, the marks awarded for the question will be 0.
Calculate the marks obtained by the student and print this as float value.
The input contains four lines.
(1) First line is the number of marks for the question.
(2) Second line contains the number of options for the question.
(3) Third line is a comma-separated sequence of correct options for this question.
(4) Fourth line is a comma-separated sequence of options given by the student.
Write a program to print the number of marks scored by a student.
"""
marks=abs(int(input()))
options=abs(int(input()))
correct_options=str(input())
student_options=str(input())
correct_options_list=correct_options.split(",")
student_options_list=student_options.split(",")
score=0

for o in student_options_list:
    if o in correct_options_list:
        mark=marks/len(correct_options_list)
        score+=mark
    else:
        score=0
        break
        
print(f"{score:.1f}")        



