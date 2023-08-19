import tkinter as tk
import tkinter.messagebox
import pyperclip

def generate_message():
    name = name_entry.get()
    industry = industry_entry.get()

    if name and industry:
        message = f"Let's Connect on LinkedIn!\n\nHi {name},\n\nHope you're doing well! I came across your profile and thought it would be great to connect. Your background in {industry} is impressive. Let's expand our professional networks!\n\nBest,\nJetur Gavli"
        message_text.delete(1.0, tk.END)  # Clear previous content
        message_text.insert(tk.END, message)
    else:
        tkinter.messagebox.showwarning("Warning", "Please enter your name and the recipient's industry.")

def copy_to_clipboard():
    message = message_text.get(1.0, tk.END)
    pyperclip.copy(message)
    tkinter.messagebox.showinfo("Copied", "Message copied to clipboard!")

def clear_fields():
    name_entry.delete(0, tk.END)
    industry_entry.delete(0, tk.END)
    message_text.delete(1.0, tk.END)

# Create the main window
window = tk.Tk()
window.title("LinkedIn Connection Message Generator")

# Create and place widgets
name_label = tk.Label(window, text="Your Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

industry_label = tk.Label(window, text="Recipient's Industry:")
industry_label.pack()
industry_entry = tk.Entry(window)
industry_entry.pack()

generate_button = tk.Button(window, text="Generate Message", command=generate_message)
generate_button.pack()

message_text = tk.Text(window, height=10, width=50)
message_text.pack()

copy_button = tk.Button(window, text="Copy Message", command=copy_to_clipboard)
copy_button.pack()

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack()

# Start the GUI event loop
window.mainloop()
