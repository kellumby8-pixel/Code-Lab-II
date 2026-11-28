# CAUTION:
# These codes for game wasn't copied from any sort of Ai Agent.
# Got help from multiple youtube video.
# AI was used at the very end to fix the error and identation mistakes.
# Color palette from pinterest.

from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image

# --- Window & Background Setup ---
root = Tk()
root.title("Math Quiz")
root.geometry("420x340")
root.iconbitmap("flower_leaf_spring_autumn_garden_nature_ecology_environment_plants_herb_flora_bloom_blossom_petal_icon_153841.ico")
root.resizable(False, False)

bg_photo = ImageTk.PhotoImage(Image.open("Image2.jpg").resize((420, 340)))

# --- Game Variables ---
level = 1
score = 0
question_count = 0
tries = 1
answer = 0

# --- Helper Functions ---
def show_screen(screen):
    for s in (welcome_canvas, menu_canvas, quiz_canvas, result_canvas):
        s.pack_forget()
    screen.pack(fill="both", expand=True)

def go_home():
    if messagebox.askyesno("Quit Quiz", "Are you sure you want to return to the Home page? Your current progress will be lost."):
        show_screen(welcome_canvas)

def start_game(chosen_level):
    global level, score, question_count
    level, score, question_count = chosen_level, 0, 0
    show_screen(quiz_canvas)
    next_problem()

def next_problem():
    global question_count, tries, answer
    if question_count == 10:
        show_results()
        return

    question_count += 1
    tries = 1

    # Pick numbers based on level
    ranges = {1: (1, 9), 2: (10, 99), 3: (10000, 99999)}
    low, high = ranges[level]
    num1, num2 = random.randint(low, high), random.randint(low, high)
    sign = random.choice(["+", "-"])
    answer = num1 + num2 if sign == "+" else num1 - num2

    # Update screen
    status_label.config(text=f"Question {question_count}/10 | Score: {score}")
    quiz_canvas.itemconfig(problem_text, text=f"{num1} {sign} {num2} =")
    quiz_canvas.itemconfig(hint_text, text="")
    user_input.delete(0, END)
    user_input.focus()

def check_answer():
    global score, tries
    try:
        user_num = int(user_input.get().strip())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please Enter A Number!")
        user_input.delete(0, END)
        return

    if user_num == answer:
        points = 10 if tries == 1 else 5
        title = "Correct!" if tries == 1 else "Correct! (2nd Attempt)"
        score += points
        messagebox.showinfo(title, f"Great job! You got {points} points." if tries == 1 else f"You got {points} points.")
        next_problem()
    elif tries == 1:
        tries = 2
        quiz_canvas.itemconfig(hint_text, text="Incorrect! You have 1 chance left.")
        user_input.delete(0, END)
    else:
        messagebox.showinfo("Wrong :(", f"Incorrect again! The answer was {answer}.")
        next_problem()

def show_results():
    show_screen(result_canvas)
    if score >= 90: grade = "A+"
    elif score >= 80: grade = "A"
    elif score >= 70: grade = "B"
    elif score >= 60: grade = "C"
    elif score >= 50: grade = "D"
    else: grade = "F"

    result_canvas.itemconfig(final_score_text, text=f"Final Score: {score}/100")
    result_canvas.itemconfig(grade_text, text=f"Rank: {grade}")

def create_screen():
    canvas = Canvas(root, width=420, height=340, highlightthickness=0)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    return canvas

# --- Screen 1: Welcome ---
welcome_canvas = create_screen()
welcome_canvas.create_text(210, 85, text="MATH QUIZ", font=("Georgia", 22, "bold"), fill="#0F090C")
welcome_canvas.create_text(210, 125, text="Test your mental math skills", font=("Helvetica", 10), fill="#000000")
start_btn = Button(root, text="START QUIZ", font=("Helvetica", 11, "bold"), bg="#D95988", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=lambda: show_screen(menu_canvas))
welcome_canvas.create_window(210, 195, window=start_btn)

# --- Screen 2: Difficulty Menu ---
menu_canvas = create_screen()
menu_canvas.create_text(210, 60, text="SELECT DIFFICULTY", font=("Georgia", 15, "bold"), fill="#000000")

levels = [("1. Easy", 1, 125), ("2. Moderate", 2, 180), ("3. Advanced", 3, 235)]
for text, lvl, y_pos in levels:
    btn = Button(root, text=text, font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=18, pady=8, cursor="hand2", command=lambda l=lvl: start_game(l))
    menu_canvas.create_window(210, y_pos, window=btn)

# --- Screen 3: Quiz ---
quiz_canvas = create_screen()

top_bar = Frame(root, bg="#4A3F4B", width=420, height=38)
top_bar.pack_propagate(False)
status_label = Label(top_bar, text="Question 1/10 | Score: 0", font=("Helvetica", 10, "bold"), bg="#4A3F4B", fg="#C1A0AC", padx=12)
status_label.pack(side="left", fill="y")
home_btn = Button(top_bar, text="Home", font=("Helvetica", 9, "bold"), bg="#806C79", fg="#F0D9E4", activebackground="#C1A0AC", activeforeground="#16131F", relief="flat", padx=10, pady=2, cursor="hand2", command=go_home)
home_btn.pack(side="right", padx=10, pady=6)
quiz_canvas.create_window(210, 19, window=top_bar)

problem_text = quiz_canvas.create_text(210, 105, text="", font=("Georgia", 22, "bold"), fill="#020102")
user_input = Entry(root, font=("Helvetica", 14, "bold"), width=12, justify="center", bg="#F0D9E4", fg="#16131F", insertbackground="#16131F", relief="flat", highlightthickness=2, highlightbackground="#806C79", highlightcolor="#C1A0AC")
quiz_canvas.create_window(210, 160, window=user_input, height=34)
submit_btn = Button(root, text="Submit", font=("Helvetica", 11, "bold"), bg="#C1A0AC", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=14, pady=8, cursor="hand2", command=check_answer)
quiz_canvas.create_window(210, 220, window=submit_btn)
hint_text = quiz_canvas.create_text(210, 265, text="", font=("Helvetica", 10, "italic"), fill="#C1A0AC")

# --- Screen 4: Results ---
result_canvas = create_screen()
result_canvas.create_text(210, 65, text="Quiz Complete!", font=("Georgia", 18, "bold"), fill="#6B324E")
final_score_text = result_canvas.create_text(210, 110, text="", font=("Helvetica", 13), fill="#773A51")
grade_text = result_canvas.create_text(210, 145, text="", font=("Georgia", 16, "bold"), fill="#080408")
play_again_btn = Button(root, text="Play Again", font=("Helvetica", 11, "bold"), bg="#C1A0AC", fg="#16131F", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=lambda: show_screen(menu_canvas))
quit_btn = Button(root, text="Quit", font=("Helvetica", 11, "bold"), bg="#4A3F4B", fg="#F0D9E4", activebackground="#806C79", activeforeground="#F0D9E4", relief="flat", width=16, pady=8, cursor="hand2", command=root.destroy)
result_canvas.create_window(210, 205, window=play_again_btn)
result_canvas.create_window(210, 255, window=quit_btn)

# --- Start App ---
show_screen(welcome_canvas)
root.mainloop()

