from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)

# ---------------------------- SAVING INFO ------------------------------- #
def search():
    website = entry_website.get().lower()
    if website == '':
        messagebox.showerror("Error","Enter the website name for searching!")
    else:
        try:
            with open("database.json", mode="r") as database:
                password_db = json.load(database)
        except FileNotFoundError:
            messagebox.showerror("Error", "You have no saved passwords!")
        else:
            try:
                messagebox.showinfo("Search results", f"Website: {website}\n"
                                                      f"username: {password_db[website]["username"]}\n"
                                                      f"password: {password_db[website]["password"]}")
            except:
                messagebox.showerror("Error", "There is no info for this website!")

    pass
def clear_entries():
    entry_username.delete(0,END)
    entry_username.insert(0, "@gmail.com")
    entry_website.delete(0,END)
    entry_password.delete(0,END)

def save_password():
    website = entry_website.get().lower()
    username = entry_username.get()
    password = entry_password.get()
    # check whether all entries are filled
    if website != "" and username != "" and password != "":
        # asking for confirmation
        if messagebox.askokcancel(title="Confirmation", message=f"This are your details:\n"
                                                                f"Website : {website}\n"
                                                                f"Username : {username}\n"
                                                                f"Password : {password}"):
            new_info = {website: {"username": username, "password": password}}
            try:
                with open("database.json", mode="r") as database:
                    password_db = json.load(database)
            except FileNotFoundError:
                with open("database.json", mode="w") as database:
                    json.dump(new_info, database, indent=4)
            else:
                password_db.update(new_info)
                with open("database.json", mode="w") as database:
                    json.dump(password_db,database,indent=4)
            finally:
                clear_entries()
        else:
            messagebox.showinfo(title="Error", message="You missed something")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

canvas = Canvas(height=200, width=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

label_1 = Label(text="Website")
label_1.grid(row=1,column=0)
label_2 = Label(text="Email/Username")
label_2.grid(row=2,column=0)
label_3 = Label(text="Password")
label_3.grid(row=3,column=0)

entry_website = Entry(width=34)
entry_website.grid(row=1,column=1)
entry_website.focus()
entry_username = Entry(width=55)
entry_username.grid(row=2,column=1,columnspan=2)
entry_username.insert(0,"@gmail.com")
entry_password = Entry(width=34)
entry_password.grid(row=3,column=1)

button_search = Button(width=16,text="Search",command=search)
button_search.grid(row=1,column=2)
button_generator = Button(width=16,text="Generate Password",command=generate_password)
button_generator.grid(row=3,column=2)
button_add = Button(width=46,text="Add",command=save_password)
button_add.grid(row=4,column=1,columnspan=2)

window.mainloop()