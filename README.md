# TuFFSnatcher

TuFFSnatcher is a Python-based tool designed for extracting Wi-Fi passwords and performing Gmail brute force attacks. It provides a simple GUI using Tkinter and relies on threading for efficient execution.

## Features
- Extracts stored Wi-Fi passwords from the system.
- Attempts Gmail brute force attacks using a custom or pre-made password list.
- Supports both custom-made `password.txt` files or the popular `rockyou.txt` wordlist.

### Disclaimer
**This tool is for educational purposes only.** The author will not be held accountable for any misuse or illegal activity resulting from the use of this tool. Always obtain proper authorization before testing or extracting credentials.

## Requirements
Ensure you have Python 3 installed. The following Python packages are required:

- Tkinter (for the graphical user interface)
- smtplib (for email interactions)
- PIL (Python Imaging Library)
- subprocess (to run system commands)
- re (for regular expressions)
- threading (for managing concurrent tasks)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dkhacker707/TuFFSnatcher.git
   cd TuFFSnatcher
