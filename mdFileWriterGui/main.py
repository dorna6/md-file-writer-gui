import tkinter as tk

# init tkinter
root = tk.Tk()

# set window size and label
root.geometry("1100x700")
root.title("md file writer")

label = tk.Label(root, text="welcome")
label.pack(padx=20,pady=20)

textbox = tk.Text(root)
textbox.pack()

# start loop
root.mainloop()