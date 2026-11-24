# CAUTION:
#These codes for game wasn't copied from any sort of Ai Agent.
#Got help from multiple youtube video.
# AI was used at the very end to fix the error and identation mistakes.
# Color palette from pinterest.

from tkinter import *
from tkinter import messagebox
import random

# Window Page
root = Tk()
root.title("Math Quiz")
root.geometry("420x340")
root.iconbitmap("flower_leaf_spring_autumn_garden_nature_ecology_environment_plants_herb_flora_bloom_blossom_petal_icon_153841.ico")
root.configure(bg="#16131F")


def displayMenu():
    welcome_frame.pack_forget()
    result_frame.pack_forget()
    menu_frame.pack(fill="both", expand=True)


# Variables
level = 1
score = 0
question_count = 0
tries = 1
answer = 0


def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    else:
        return random.randint(10000, 99999)


def decideOperation():
    return random.choice(["+", "-"])

def easy():
    start_game(1)

def moderate():
    start_game(2)

def advanced():
    start_game(3)

def start_game(choosen_level):
    global level, score, question_count
    level = choosen_level
    score = 0
    question_count = 0
    menu_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    displayProblem()


# Show new math problem
def displayProblem():
    global question_count, tries, answer
    if question_count == 10:
        displayResults()
        return

    question_count += 1
    tries = 1
    num1 = randomInt(level)
    num2 = randomInt(level)
    sign = decideOperation()

    if sign == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2

    status_label.config(text=f"Question {question_count}/10   |   Score: {score}", bg="#4A3F4B", fg="#C1A0AC")
    problem_label.config(text=f"{num1} {sign} {num2} =", bg="#16131F", fg="#F0D9E4")
    hint_label.config(text="", bg="#16131F", fg="#C1A0AC")
    user_input.delete(0, END)
    user_input.focus()

# Checking if user answer is correct
def Correct():
    global score, tries
    typed = user_input.get().strip()

    if not typed.lstrip("-").isdigit():
        messagebox.showwarning("Invalid Input", "Please Enter A Number!")
        user_input.delete(0, END)
        return

    user_num = int(typed)
    if user_num == answer:
        if tries == 1:
            score += 10
            messagebox.showinfo("Correct!", "Great job! You got 10 points.")
        else:
            score += 5
            messagebox.showinfo("Correct! (2nd Attempt)", "You got 5 points.")
        displayProblem()
    else:
        if tries == 1:
            tries = 2
            hint_label.config(text="Incorrect! You have 1 chance left.", fg="#C1A0AC", bg="#16131F")
            user_input.delete(0, END)
        else:
            messagebox.showinfo("Wrong :(", f"Incorrect again! The answer was {answer}.")
            displayProblem()

# Switch from quiz frame to result frame and show final score
def displayResults():
    quiz_frame.pack_forget()
    result_frame.pack(fill="both", expand=True)

    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    final_score_label.config(text=f"Final Score: {score}/100", bg="#16131F", fg="#C1A0AC")
    grade_label.config(text=f"Rank: {grade}", bg="#16131F", fg="#F0D9E4")

# Frame 1: Welcome Frame
welcome_frame = Frame(root, bg="#16131F")
Label(welcome_frame, text=" MATH QUIZ ", font=("Georgia", 22, "bold"), bg="#16131F", fg="#F0D9E4").pack(pady=(55, 10))
Label(welcome_frame, text="Test your mental math skills", font=("Helvetica", 10), bg="#16131F", fg="#C1A0AC").pack(pady=(0, 35))
Button(welcome_frame, text="START QUIZ", font=("Helvetica", 11, "bold"), bg="#C1A0AC", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=displayMenu).pack()

# Frame 2: Difficulty Menu Frame
menu_frame = Frame(root, bg="#16131F")
Label(menu_frame, text="SELECT DIFFICULTY", font=("Georgia", 15, "bold"), bg="#16131F", fg="#F0D9E4").pack(pady=(35, 20))
Button(menu_frame, text="1. Easy", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=18, pady=8, cursor="hand2", command=easy).pack(pady=6)
Button(menu_frame, text="2. Moderate", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=18, pady=8, cursor="hand2", command=moderate).pack(pady=6)
Button(menu_frame, text="3. Advanced", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=18, pady=8, cursor="hand2", command=advanced).pack(pady=6)

# Frame 3: Quiz Frame
quiz_frame = Frame(root, bg="#16131F")
status_label = Label(quiz_frame, text="Question 1/10   |   Score: 0", font=("Helvetica", 10, "bold"), bg="#4A3F4B", fg="#C1A0AC", pady=8)
status_label.pack(fill="x")

problem_label = Label(quiz_frame, text="", font=("Georgia", 22, "bold"), bg="#16131F", fg="#F0D9E4")
problem_label.pack(pady=(35, 15))

user_input = Entry(quiz_frame, font=("Helvetica", 14, "bold"), width=12, justify="center", bg="#F0D9E4", fg="#16131F", insertbackground="#16131F", relief="flat", highlightthickness=2, highlightbackground="#806C79", highlightcolor="#C1A0AC")
user_input.pack(pady=5, ipady=4)

Button(quiz_frame, text="Submit", font=("Helvetica", 11, "bold"), bg="#C1A0AC", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=14, pady=8, cursor="hand2", command=Correct).pack(pady=15)
hint_label = Label(quiz_frame, text="", font=("Helvetica", 10, "italic"), bg="#16131F", fg="#C1A0AC")
hint_label.pack(pady=2)

# Frame 4: Results Frame
result_frame = Frame(root, bg="#16131F")
Label(result_frame, text="Quiz Complete!", font=("Georgia", 18, "bold"), bg="#16131F", fg="#F0D9E4").pack(pady=(30, 10))
final_score_label = Label(result_frame, text="", font=("Helvetica", 13), bg="#16131F", fg="#C1A0AC")
final_score_label.pack(pady=5)
grade_label = Label(result_frame, text="", font=("Georgia", 16, "bold"), bg="#16131F", fg="#F0D9E4")
grade_label.pack(pady=(5, 20))

Button(result_frame, text="Play Again", font=("Helvetica", 11, "bold"), bg="#C1A0AC", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=displayMenu).pack(pady=5)
Button(result_frame, text="Quit", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=root.destroy).pack(pady=5)

# Show the first frame when the app opens
welcome_frame.pack(fill="both", expand=True)
root.mainloop()




