import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import cv2  # Import OpenCV
from classify import classify_image
from PIL import Image, ImageTk  # Only needed to display images in Tkinter

# Connect to SQLite Database
conn = sqlite3.connect("fruit_classifier.db")
cursor = conn.cursor()

# Create users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# ---------- LOGIN SYSTEM ----------
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    
    if user:
        messagebox.showinfo("Login Success", "Welcome!")
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    username = entry_username.get()
    password = entry_password.get()
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Registration Success", "You can now log in!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

# ---------- IMAGE CLASSIFICATION ----------
def upload_image():
    file_path = filedialog.askopenfilename(parent=root)
    if file_path:
        result = classify_image(file_path)
        label_result.config(text=f"Result: {result}")

        # Load image using OpenCV
        img = cv2.imread(file_path)

        if img is None:
            messagebox.showerror("Error", "Cannot read image file!")
            return

        # Convert to RGB (since OpenCV loads in BGR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Resize for display
        img = cv2.resize(img, (300, 300))

        # Convert OpenCV image to Tkinter-compatible format
        img = Image.fromarray(img)  # Convert numpy array to Image
        img = ImageTk.PhotoImage(img)  # Convert Image to Tkinter format

        # Update GUI
        image_label.config(image=img)
        image_label.image = img

# ---------- MAIN APPLICATION WINDOW ----------
def open_main_window():
    global root
    root = tk.Tk()
    root.title("Fruit Classifier")
    root.geometry("600x700")

    # Upload Button
    btn_upload = tk.Button(root, text="📂 Upload Image", command=upload_image,
                            font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", 
                            width=20, height=2)
    btn_upload.pack(pady=20)

    # Image Label
    global image_label
    image_label = tk.Label(root, bg="white", width=400, height=400, relief="solid", borderwidth=3)
    image_label.pack(pady=10)

    # Result Label
    global label_result
    label_result = tk.Label(root, text="Result: ", font=("Arial", 20, "bold"), bg="black", fg="white", width=25, height=2)
    label_result.pack(pady=15)

    root.mainloop()

# ---------- LOGIN WINDOW ----------
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x300")

tk.Label(login_window, text="Username:", font=("Arial", 14)).pack(pady=5)
entry_username = tk.Entry(login_window, font=("Arial", 14))
entry_username.pack(pady=5)

tk.Label(login_window, text="Password:", font=("Arial", 14)).pack(pady=5)
entry_password = tk.Entry(login_window, font=("Arial", 14), show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(login_window, text="Login", command=login, font=("Arial", 14), bg="#4CAF50", fg="white", width=10)
btn_login.pack(pady=10)

btn_register = tk.Button(login_window, text="Register", command=register, font=("Arial", 14), bg="#2196F3", fg="white", width=10)
btn_register.pack(pady=10)

login_window.mainloop()

# Close database connection when app is closed
conn.close()
