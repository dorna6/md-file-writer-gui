import tkinter as tk

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Frame Switching Example")

# Create buttons
button1 = tk.Button(root, text="Frame 1", command=lambda: show_frame(frame1))
button2 = tk.Button(root, text="Frame 2", command=lambda: show_frame(frame2))
button3 = tk.Button(root, text="Frame 3", command=lambda: show_frame(frame3))

button1.pack(side="left", padx=10, pady=10)
button2.pack(side="left", padx=10, pady=10)
button3.pack(side="left", padx=10, pady=10)

# Create frames
frame1 = tk.Frame(root, width=400, height=300, bg="lightblue")
frame2 = tk.Frame(root, width=400, height=300, bg="lightgreen")
frame3 = tk.Frame(root, width=400, height=300, bg="lightcoral")

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=0, column=0, sticky="nsew")

# Initially hide frames 2 and 3
frame2.grid_forget()
frame3.grid_forget()

root.mainloop()
