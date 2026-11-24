from tkinter import *
import random
from PIL import ImageTk, Image 

# Window Page:
root = Tk()
root.title("Alexa Tell Me A Joke")
root.geometry("450x350")
root.iconbitmap("flower_leaf_spring_autumn_garden_nature_ecology_environment_plants_herb_flora_bloom_blossom_petal_icon_153841.ico")
root.resizable(False, False) #Locked window size so the background stays fit.

# Adding Image and resizing it:
bg_image = Image.open("pic1.jpg")
resized_image = bg_image.resize((450, 350))
bg_photo = ImageTk.PhotoImage(resized_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#File handling. This will open the text file and 
# save all the jokes into a list::
jokes = []
with open("randomJokes.txt", "r") as file:
    for line in file:
        if"?" in line:
            jokes.append(line.strip())

# Variable: it will remember the answer for the current joke:
current_punchline = ""

# It will run when the user click on "Alexa Tell Me A Joke" or "Next Joke"
def get_joke():
    global current_punchline

   #Pick random joke from the list
    chosen_joke = random.choice(jokes)
   #Split it into 2 pieces: [0] setup and [1] punchline/Answer.
    parts = chosen_joke.split("?", 1) 

    setup = parts[0] + "?"
    current_punchline = parts[1]

# It will show the question on the screen and clear the old answer.
    setup_label.config(text=setup)
    punchline_label.config(text="") 

# It will run when the user click on "Show Punchline"
def show_punchline():
    punchline_label.config(text=current_punchline)

Ask_button = Button(root, text="Alexa tell me a Joke",
             font=("Ariel",12),command=get_joke)
Ask_button.pack(pady=15)

setup_label = Label(root,text="Press the button to hear a joke!",
                font=("Ariel",12,"bold"), wraplength=400)
setup_label.pack(pady=10)

punchline_label = Label(root, text="", font=("Ariel",12), fg="blue",
                        wraplength=400)
punchline_label.pack(pady=10)

punchline_button = Button(root,text="Show Punchline",font=("Ariel",11),
                 command=show_punchline)
punchline_button.pack(pady=5)

next_button= Button(root, text="Next Joke", font=("Ariel",11),
                    command=get_joke)
next_button.pack(pady=5)

quit_button= Button(root, text="Quit", font=("Ariel",11),
                    command=root.destroy)
quit_button.pack(pady=15)

root.mainloop()
                        #THE END :)

    