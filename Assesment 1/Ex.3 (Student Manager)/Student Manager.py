#CAUTION:
# Some code have been generated from AI called perplexity.
# Most of them have been done by me and gotten from ppt.
# The design/ layout was designed by me.
# Colour palette from pinterest.
# studentMarks.txt was already provided.

from tkinter import *
#Main window page
root = Tk()
root.title("Student Manager")
root.geometry("860x560")
root.configure(bg="#F5F0E6")

#File handling. This will open the text file 
#Saving it in form of list
students = []
with open("studentMarks.txt", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        if line.strip() != "":
            students.append(line.strip().split(","))

def get_total(student):
    roll_no, name, course1, course2, course3, exam_marks = student
    return int(course1) + int(course2) + int(course3) + int(exam_marks)

def make_report(student):
    roll_no, name, course1, course2, course3, exam_marks = student
    Course_Work = int(course1) + int(course2) + int(course3)
    Exam_Mark = int(exam_marks)
    Total = Course_Work + Exam_Mark
    Percent = (Total / 160) * 100

#-START-code from perplexity
#Assigning grades    
    if Percent >= 70:
        grade = "A"
    elif Percent >= 60:
        grade = "B"
    elif Percent >= 50:
        grade = "C"
    elif Percent >= 40:
        grade = "D"
    else:
        grade = "F"
    return (
        f"Name: {name.strip()} , Number: {roll_no.strip()}\n"
        f"CourseWork: {Course_Work}/60 , Exam: {Exam_Mark}/100\n"
        f"Percentage: {Percent:.1f}% , Grade: {grade}\n"
        f"------------------------------------------\n"
    )
  # -END- 

# Clear the main display box and show new results
def show_text(message):
    text_box.delete("1.0", END)
    text_box.insert(END, message)

#Show every student's report along with the 
# overall class average
def view_all():
    output = ""
    total_percent = 0
    for student in students:
        output += make_report(student)
        total_percent += (get_total(student) / 160) * 100

    average = total_percent / len(students)
    output += f"\nTotal Students: {len(students)} | Class Average: {average:.1f}%"
    show_text(output)

def view_one():
    search = search_box.get().strip().lower()
    
# Make sure the user actually typed something before searching.
    if search == "":
        search_box.focus_set()
        show_text("Please type a student name or roll number in the box above," \
        " \n       then click '4. View Individual Student' again.")
        return
 # Look through the list for a matching roll number or name
    for student in students:
        roll_no, name, course1, course2, course3, exam_marks = student
        if search == roll_no.strip().lower() or search in name.strip().lower():
            show_text(make_report(student))
            return
    show_text("Student not found. Try typing a valid name or student roll_no.")

#Display the student with highest score
def view_highest():
    top_student = students[0]  # Restored [0] here
    for student in students:
        if get_total(student) > get_total(top_student):
            top_student = student
    show_text("Highest Score:\n" + make_report(top_student))

 #Displays the student with lowest score   
def view_lowest():
    lowest_student = students[0]  # Restored [0] here
    for student in students:
        if get_total(student) < get_total(lowest_student):
            lowest_student = student
    show_text("Lowest Score:\n" + make_report(lowest_student))

# Heading
Label(root, text="🎓 Student Manager", font=("Georgia", 20, "bold"), bg="#F5F0E6", fg="#35495E").grid(row=0, column=0, columnspan=2, pady=(15, 0))
Label(root, text="Manage | View | Analyze", font=("Georgia", 10), bg="#F5F0E6", fg="#627D93").grid(row=1, column=0, columnspan=2, pady=(0, 20))

#Left Side Buttons:
Button(root, text="1. View All Students", width=24, font=("Georgia", 10, "bold"),
       bg="#35495E", fg="white", bd=0, pady=8, command=view_all).grid(row=2, column=0, padx=25, pady=6)

Button(root, text="2. Highest Total Score", width=24, font=("Georgia", 10, "bold"),
       bg="#627D93", fg="white", bd=0, pady=8, command=view_highest).grid(row=3, column=0, padx=25, pady=6)

Button(root, text="3. Lowest Total Score", width=24, font=("Georgia", 10, "bold"),
       bg="#B0C0CE", fg="#35495E", bd=0, pady=8, command=view_lowest).grid(row=4, column=0, padx=25, pady=6)

Button(root, text="4. View Individual Student", width=24, font=("Georgia", 10, "bold"),
       bg="#D8E0E8", fg="#35495E", bd=0, pady=8, command=view_one).grid(row=5, column=0, padx=25, pady=6)

#Big Text Box
Label(root, text="Enter Student Name or Roll_No:", font=("Georgia", 10, "italic"), bg="#F5F0E6", fg="#35495E").grid(row=2, column=1, sticky="w", padx=10)

search_box = Entry(root, width=52, font=("Georgia", 10), bg="white", fg="#35495E")
search_box.grid(row=3, column=1, sticky="w", padx=10, ipady=4)

text_box = Text(root, width=62, height=20, font=("Consolas", 10), bg="#DCE3EC", fg="#35495E", bd=1, padx=12, pady=12)
text_box.grid(row=4, column=1, rowspan=5, padx=10, pady=(10, 20))

root.mainloop()
