import tkinter as tk
from fnmatch import fnmatch

def reply_msg(msg):
    if fnmatch(msg, '*hello*') or fnmatch(msg, '*good morning*'):
        return 'Hello'
    elif fnmatch(msg, '*what*you*name*'):
        return 'My name is OSS Chatbot.'
    return "I don't understand your words."

def handle_button_send():
    text_dialog.insert('end', 'You: ' + entry_msg.get() + '\n')
    text_dialog.insert('end', 'Bot: ' + reply_msg(entry_msg.get()) + '\n')
    entry_msg.delete(0, tk.END)

root = tk.Tk()
root.title('A Very Simple Chatbot')
label = tk.Label(root, text='Chat Dialog')
label.pack()
text_dialog = tk.Text(root)
text_dialog.pack()
label = tk.Label(root, text='Your Message:')
label.pack()
entry_msg = tk.Entry(root)
entry_msg.pack()
button_send = tk.Button(root, text='Send Your Message', command=handle_button_send)
button_send.pack()

root.mainloop()