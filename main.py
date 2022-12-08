from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)

web_entry = Entry(width=35)
web_entry.grid(column=1, columnspan=2, row=1)

user_entry = Entry(width=35)
user_entry.grid(column=1, columnspan=2, row=2)

pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

generate_button = Button(text="Add", width=36)
generate_button.grid(column=1, columnspan=2, row=4)

window.mainloop()