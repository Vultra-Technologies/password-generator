import string
import random
import tkinter as tk
from tkinter import messagebox, filedialog

def generate_password():
    length = int(length_entry.get())
    characterList = ""

    if digits_var.get():
        characterList += string.digits
    if letters_var.get():
        characterList += string.ascii_letters
    if special_var.get():
        characterList += string.punctuation

    if not characterList:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = [random.choice(characterList) for _ in range(length)]
    password_str = "".join(password)
    password_label.config(text=f"Generated Password: {password_str}")

def save_password():
    if password_label.cget("text") == "":
        messagebox.showerror("Error", "Generate a password first.")
        return

    savepwd = messagebox.askyesno("Save Password", "Do you want to save your password?")
    if savepwd:
        pwdname = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if pwdname:
            with open(pwdname, "w") as file:
                file.write(password_label.cget("text"))
            messagebox.showinfo("Success", f"Saved successfully as {pwdname}")
        else:
            messagebox.showwarning("Warning", "No file selected. Password not saved.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Styling
root.configure(bg="#f0f0f0")
root.geometry("400x300")

# Widgets
length_label = tk.Label(root, text="Enter password length:", bg="#f0f0f0")
length_entry = tk.Entry(root)
length_label.pack(pady=10)
length_entry.pack()

digits_var = tk.BooleanVar()
letters_var = tk.BooleanVar()
special_var = tk.BooleanVar()

digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var, bg="#f0f0f0")
letters_check = tk.Checkbutton(root, text="Letters", variable=letters_var, bg="#f0f0f0")
special_check = tk.Checkbutton(root, text="Special characters", variable=special_var, bg="#f0f0f0")

digits_check.pack(anchor="w")
letters_check.pack(anchor="w")
special_check.pack(anchor="w")

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#007acc", fg="white")
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", bg="#f0f0f0", font=("Ubuntu", 12))
password_label.pack()

save_button = tk.Button(root, text="Save Password", command=save_password, bg="#007acc", fg="white")
save_button.pack(pady=10)

root.mainloop()
