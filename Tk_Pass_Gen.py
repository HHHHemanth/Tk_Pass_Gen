import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = ttk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.accept_button = ttk.Button(root, text="Accept Password", command=self.accept_password, state=tk.DISABLED)
        self.accept_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.reset_button = ttk.Button(root ,text="Reset", command=self.reset)
        self.reset_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.password_label = ttk.Label(root, text="Generated Password:")
        self.password_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.complexity_label = ttk.Label(root , text="Password Complexity: 0%")
        self.complexity_label.grid(row=4, column=0, columnspan=3, pady=10)

        self.accepted_password = ""

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be greater than 0")

            password = self.generate_random_password(length)
            self.password_label.config(text=f"Generated Password: {password}")
            self.accept_button.config(state=tk.NORMAL)

            complexity_percentage = self.calculate_complexity(password)
            self.complexity_label.config(text=f"Password Complexity: {complexity_percentage}%")

            self.accepted_password = ""  

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def calculate_complexity(self, password):
        uppercase = any(c.isupper() for c in password)
        lowercase = any(c.islower() for c in password)
        digits = any(c.isdigit() for c in password)
        special_characters = any(c in string.punctuation for c in password)

        complexity_percentage = sum([uppercase, lowercase, digits, special_characters]) * 25
        return complexity_percentage

    def accept_password(self):
        self.accepted_password = self.password_label.cget("text").split(": ")[1]
        messagebox.showinfo("Accepted", "Password accepted!")

    def reset(self):
        self.length_entry.delete(0, tk.END)
        self.password_label.config(text="Generated Password:")
        self.complexity_label.config(text="Password Complexity: 0%")
        self.accept_button.config(state=tk.DISABLED)
        self.accepted_password = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
