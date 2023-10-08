import tkinter as tk

class AnimatedFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.counter = 0
        self.label = tk.Label(self, text="Counter: 0")
        self.label.pack()

    def update_counter(self):
        self.counter += 1
        self.label.config(text=f"Counter: {self.counter}")
        self.after(1000, self.update_counter)  # Schedule this method to run after 1 second

if __name__ == "__main__":
    root = tk.Tk()
    frame = AnimatedFrame(root)
    frame.pack()
    frame.update_counter()
    root.mainloop()
