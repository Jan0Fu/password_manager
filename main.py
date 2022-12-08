from tkinter import *



def save():
    website = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(127, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

web_entry = Entry(width=38)
web_entry.grid(column=1, columnspan=2, row=1)
web_entry.focus()
user_entry = Entry(width=38)
user_entry.grid(column=1, columnspan=2, row=2)
user_entry.insert(END, "janivstar@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
