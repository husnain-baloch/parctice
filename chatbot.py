import tkinter as tk
from tkinter import ttk

# Emoji reactions based on user message
def get_emoji_response(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "👋"
    elif any(word in user_input for word in ["happy", "good", "great", "awesome"]):
        return "😀"
    elif any(word in user_input for word in ["sad", "bad", "upset", "cry"]):
        return "😢"
    elif any(word in user_input for word in ["angry", "mad", "fight"]):
        return "😡"
    elif any(word in user_input for word in ["love", "heart"]):
        return "❤️"
    else:
        return "🤔"  # default confused face

# Function to send message
def send_message(event=None):
    user_message = entry.get()
    if user_message.strip() == "":
        return

    # Enable text box to insert
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_message}\n")

    # Get emoji response
    bot_response = get_emoji_response(user_message)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")

    # Disable editing again
    chat_area.config(state=tk.DISABLED)

    # Auto-scroll
    chat_area.yview(tk.END)
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Emoji Chatbot 🤖")
root.geometry("400x500")

# Chat display area
chat_area = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry box for typing
entry = ttk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

# Bind Enter key (global so it always works)
root.bind("<Return>", send_message)

# Send button
send_btn = ttk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=5)

# Focus cursor on entry when program starts
entry.focus()

# Start GUI loop
root.mainloop()
