import tkinter as tk
from tkinter import messagebox
import json
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return {"username": self.username, "password": self.password}

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data["username"], json_data["password"])


class Account():
    user = User("", "")
    def register_user(username, password):
        user = User(username, password)
        new_user_data = user.to_json()
        with open("users.json", "r+") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = {"users": []}
            data["users"].append(new_user_data)
            file.seek(0)
            json.dump(data, file, indent=4)

    def register_user_Window():
        username = username_entry.get()
        password = Encoder.encode(password_entry.get())
        User.register_user(username, password)
        messagebox.showinfo("Регистрация", "Пользователь успешно зарегистрирован.")

    def login():
        username = username_entry.get()
        password = Encoder.encode(password_entry.get())
        users = User.load_users()
        for user in users:
            if user.username == username and Encoder.compare_passwords(user.password, password):
                messagebox.showinfo("Вход", "Вход выполнен успешно.")
                return
        messagebox.showerror("Ошибка", "Неправильное имя пользователя или пароль.")


class Encoder:
    @staticmethod
    def encode(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def compare_passwords(hashed_password, input_password):
        return hashed_password == input_password


class Database:
    @staticmethod
    def migrate():
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
                users_data = data.get("users", [])
                return [User.from_json(user_data) for user_data in users_data]
        except FileNotFoundError:
            return []

# Создание графического интерфейса
def App():
    root = tk.Tk()
    Database.migrate()
    accManager = Account()
    root.title("Простое приложение")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    label_username = tk.Label(frame, text="Имя пользователя:")
    label_username.grid(row=0, column=0, sticky="e")

    username_entry = tk.Entry(frame)
    username_entry.grid(row=0, column=1)

    label_password = tk.Label(frame, text="Пароль:")
    label_password.grid(row=1, column=0, sticky="e")

    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1)

    register_button = tk.Button(frame, text="Регистрация", command=accManager.register_user_Window)
    register_button.grid(row=2, column=0, pady=5)

    login_button = tk.Button(frame, text="Вход", command=accManager.login)
    login_button.grid(row=2, column=1, pady=5)

    root.mainloop()


App()