import tkinter as tk
from tkinter import messagebox
from models.user import User
from models.reservation import Reservation
from init_db import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Crear la base de datos
engine = create_engine('sqlite:///site.db')
db.Session = sessionmaker(bind=engine)
db.Base.metadata.create_all(engine)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hotel Reservations")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Hotel 'Los Anturios'")
        self.label.pack(pady=10)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack(pady=5)

        self.reservations_button = tk.Button(self, text="Reservations", command=self.reservations)
        self.reservations_button.pack(pady=5)

    def login(self):
        login_window = tk.Toplevel(self)
        login_window.title("Login")
        login_window.geometry("300x200")

        tk.Label(login_window, text="Username").pack(pady=5)
        username_entry = tk.Entry(login_window)
        username_entry.pack(pady=5)

        tk.Label(login_window, text="Password").pack(pady=5)
        password_entry = tk.Entry(login_window, show="*")
        password_entry.pack(pady=5)

        tk.Button(login_window, text="Login", command=lambda: self.perform_login(username_entry.get(), password_entry.get())).pack(pady=10)

    def perform_login(self, username, password):
        session = db.Session()
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            messagebox.showinfo("Login Successful", f"Welcome {user.username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def register(self):
        register_window = tk.Toplevel(self)
        register_window.title("Register")
        register_window.geometry("300x200")

        tk.Label(register_window, text="Username").pack(pady=5)
        username_entry = tk.Entry(register_window)
        username_entry.pack(pady=5)

        tk.Label(register_window, text="Email").pack(pady=5)
        email_entry = tk.Entry(register_window)
        email_entry.pack(pady=5)

        tk.Label(register_window, text="Password").pack(pady=5)
        password_entry = tk.Entry(register_window, show="*")
        password_entry.pack(pady=5)

        tk.Button(register_window, text="Register", command=lambda: self.perform_register(username_entry.get(), email_entry.get(), password_entry.get())).pack(pady=10)

    def perform_register(self, username, email, password):
        session = db.Session()
        new_user = User(username=username, email=email, password=password)
        session.add(new_user)
        session.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully!")

    def reservations(self):
        reservations_window = tk.Toplevel(self)
        reservations_window.title("Reservations")
        reservations_window.geometry("300x200")

        tk.Label(reservations_window, text="Reservations will be managed here").pack(pady=20)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
