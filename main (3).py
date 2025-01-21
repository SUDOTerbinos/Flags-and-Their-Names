import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io

COUNTRIES = [
    {"name": "Ethiopia", "flag_url": "https://flagcdn.com/w320/et.png"},
    {"name": "United States", "flag_url": "https://flagcdn.com/w320/us.png"},
    {"name": "Germany", "flag_url": "https://flagcdn.com/w320/de.png"},
    {"name": "Japan", "flag_url": "https://flagcdn.com/w320/jp.png"},
    {"name": "India", "flag_url": "https://flagcdn.com/w320/in.png"},
]

class FlagViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flags and Their Names")
        self.root.geometry("400x400")

        self.current_index = 0

        self.flag_label = tk.Label(self.root)
        self.flag_label.pack(pady=10)

        self.country_name_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.country_name_label.pack(pady=10)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        self.prev_button = ttk.Button(button_frame, text="Previous", command=self.show_previous)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = ttk.Button(button_frame, text="Next", command=self.show_next)
        self.next_button.grid(row=0, column=1, padx=10)

        self.show_flag()

    def show_flag(self):
        country = COUNTRIES[self.current_index]

        response = requests.get(country["flag_url"])
        flag_image = Image.open(io.BytesIO(response.content))
        flag_image = flag_image.resize((200, 120), Image.ANTIALIAS)
        flag_photo = ImageTk.PhotoImage(flag_image)

        self.flag_label.configure(image=flag_photo)
        self.flag_label.image = flag_photo
        self.country_name_label.config(text=country["name"])

    def show_previous(self):
        self.current_index = (self.current_index - 1) % len(COUNTRIES)
        self.show_flag()

    def show_next(self):
        self.current_index = (self.current_index + 1) % len(COUNTRIES)
        self.show_flag()


if __name__ == "__main__":
    root = tk.Tk()
    app = FlagViewerApp(root)
    root.mainloop()
