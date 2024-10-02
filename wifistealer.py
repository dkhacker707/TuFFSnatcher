import subprocess
import re
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
import threading

def extract_wifi_passwords():
    extract_button.config(state=tk.DISABLED)
    status_label.config(text="Extracting passwords, please wait...")
    output_area.delete(1.0, tk.END)  
    
    def run_extraction():
        try:
            command1 = "netsh wlan show profile"
            networks = subprocess.check_output(command1, shell=True).decode('utf-8')
            networks_list = re.findall(r'Profile\s*:\s*(.*)', networks)

            final_output = ""
            for network in networks_list:
                command2 = f"netsh wlan show profile \"{network.strip()}\" key=clear"
                one_network_result = subprocess.check_output(command2, shell=True).decode('utf-8')
                final_output += one_network_result + "\n"

            with open("wifipasswords.txt", 'w') as file:
                file.write(final_output)

            output_area.insert(tk.END, final_output)  # THIS ONE IS PRETTY HARD FOR ME its for showing GUI
            messagebox.showinfo("Success", "WiFi passwords extracted and saved to wifipasswords.txt")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            extract_button.config(state=tk.NORMAL)
            status_label.config(text="")

    threading.Thread(target=run_extraction).start()

def clear_output():
    output_area.delete(1.0, tk.END)

def copy_to_clipboard():   
    root.clipboard_clear()  
    root.clipboard_append(output_area.get(1.0, tk.END))  
    messagebox.showinfo("Copied", "Output copied to clipboard!")

root = tk.Tk()
root.title("WiFi Password Extractor")

extract_button = tk.Button(root, text="Extract WiFi Passwords", command=extract_wifi_passwords)

extract_button.pack(pady=10)


clear_button = tk.Button(root, text="Clear Output", command=clear_output)
clear_button.pack(pady=5)


copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)


status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=5)


output_area = scrolledtext.ScrolledText(root, width=60, height=20)
output_area.pack(padx=10, pady=10)


root.mainloop()
