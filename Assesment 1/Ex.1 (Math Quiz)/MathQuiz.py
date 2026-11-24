# CAUTION:
# These codes for game wasn't copied from any sort of Ai Agent.
# Got help from multiple youtube video.
# AI was used at the very end to fix the error and identation mistakes.
# Color palette from pinterest.

from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image 

# Window Page
root = Tk()
root.title("Math Quiz")
root.geometry("420x340")
root.iconbitmap("flower_leaf_spring_autumn_garden_nature_ecology_environment_plants_herb_flora_bloom_blossom_petal_icon_153841.ico")
root.resizable(False, False) # Locked window size so the background stays fit.

# Background Image (Matched to 420x340 window size)
bg_image = Image.open("Image2.jpg")
resized_image = bg_image.resize((420, 340))
bg_photo = ImageTk.PhotoImage(resized_image)

def hide_all_screens():
    welcome_canvas.pack_forget()
    menu_canvas.pack_forget()
    quiz_canvas.pack_forget()
    result_canvas.pack_forget()

def displayMenu():
    hide_all_screens()
    menu_canvas.pack(fill="both", expand=True)

def goHome():
    if messagebox.askyesno("Quit Quiz", "Are you sure you want to return to the Home page? Your current progress will be lost."):
        hide_all_screens()
        welcome_canvas.pack(fill="both", expand=True)

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
    hide_all_screens()
    quiz_canvas.pack(fill="both", expand=True)
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

    status_label.config(text=f"Question {question_count}/10 | Score: {score}")
    quiz_canvas.itemconfig(problem_text, text=f"{num1} {sign} {num2} =")
    quiz_canvas.itemconfig(hint_text, text="")
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
            quiz_canvas.itemconfig(hint_text, text="Incorrect! You have 1 chance left.")
            user_input.delete(0, END)
        else:
            messagebox.showinfo("Wrong :(", f"Incorrect again! The answer was {answer}.")
            displayProblem()

# Switch from quiz screen to result screen and show final score
def displayResults():
    hide_all_screens()
    result_canvas.pack(fill="both", expand=True)

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

    result_canvas.itemconfig(final_score_text, text=f"Final Score: {score}/100")
    result_canvas.itemconfig(grade_text, text=f"Rank: {grade}")

# --- Screen 1: Welcome Canvas ---
welcome_canvas = Canvas(root, width=420, height=340, highlightthickness=0)
welcome_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
welcome_canvas.create_text(210, 85, text="MATH QUIZ", font=("Georgia", 22, "bold"), fill="#0F090C")
welcome_canvas.create_text(210, 125, text="Test your mental math skills", font=("Helvetica", 10), fill="#000000")

start_btn = Button(root, text="START QUIZ", font=("Helvetica", 11, "bold"), bg="#D95988", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=displayMenu)
welcome_canvas.create_window(210, 195, window=start_btn)

# --- Screen 2: Difficulty Menu Canvas ---
menu_canvas = Canvas(root, width=420, height=340, highlightthickness=0)
menu_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
menu_canvas.create_text(210, 60, text="SELECT DIFFICULTY", font=("Georgia", 15, "bold"), fill="#000000")

easy_btn = Button(root, text="1. Easy", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=18, pady=8, cursor="hand2", command=easy)
mod_btn = Button(root, text="2. Moderate", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=18, pady=8, cursor="hand2", command=moderate)
adv_btn = Button(root, text="3. Advanced", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=18, pady=8, cursor="hand2", command=advanced)

menu_canvas.create_window(210, 125, window=easy_btn)
menu_canvas.create_window(210, 180, window=mod_btn)
menu_canvas.create_window(210, 235, window=adv_btn)

# --- Screen 3: Quiz Canvas ---
quiz_canvas = Canvas(root, width=420, height=340, highlightthickness=0)
quiz_canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Top bar container for Status Label + Home Button
top_bar = Frame(root, bg="#4A3F4B", width=420, height=38)
top_bar.pack_propagate(False)
status_label = Label(top_bar, text="Question 1/10 | Score: 0", font=("Helvetica", 10, "bold"), bg="#4A3F4B", fg="#C1A0AC", padx=12)
status_label.pack(side="left", fill="y")

home_btn = Button(top_bar, text="Home", font=("Helvetica", 9, "bold"), bg="#806C79", fg="#F0D9E4", activebackground="#C1A0AC", activeforeground="#16131F", relief="flat", padx=10, pady=2, cursor="hand2", command=goHome)
home_btn.pack(side="right", padx=10, pady=6)
quiz_canvas.create_window(210, 19, window=top_bar)

problem_text = quiz_canvas.create_text(210, 105, text="", font=("Georgia", 22, "bold"), fill="#020102")

user_input = Entry(root, font=("Helvetica", 14, "bold"), width=12, justify="center", bg="#F0D9E4", fg="#16131F", insertbackground="#16131F", relief="flat", highlightthickness=2, highlightbackground="#806C79", highlightcolor="#C1A0AC")
quiz_canvas.create_window(210, 160, window=user_input, height=34)

submit_btn = Button(root, text="Submit", font=("Helvetica", 11, "bold"), bg="#C1A0AC", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=14, pady=8, cursor="hand2", command=Correct)
quiz_canvas.create_window(210, 220, window=submit_btn)

hint_text = quiz_canvas.create_text(210, 265, text="", font=("Helvetica", 10, "italic"), fill="#C1A0AC")

# --- Screen 4: Results Canvas ---
result_canvas = Canvas(root, width=420, height=340, highlightthickness=0)
result_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
result_canvas.create_text(210, 65, text="Quiz Complete!", font=("Georgia", 18, "bold"), fill="#6B324E")
final_score_text = result_canvas.create_text(210, 110, text="", font=("Helvetica", 13), fill="#773A51")
grade_text = result_canvas.create_text(210, 145, text="", font=("Georgia", 16, "bold"), fill="#080408")

play_again_btn = Button(root, text="Play Again", font=("Helvetica", 11, "bold"), bg="#C1A0AC", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=displayMenu)
quit_btn = Button(root, text="Quit", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=root.destroy)

result_canvas.create_window(210, 205, window=play_again_btn)
result_canvas.create_window(210, 255, window=quit_btn)

# Show the first screen when the app opens
welcome_canvas.pack(fill="both", expand=True)

root.mainloop()
