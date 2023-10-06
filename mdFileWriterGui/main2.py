import tkinter as tk
from tkinter import ttk
import config 


element_list = [['headline1','intro'],
                ['test','welcome to my app'],
                ['headline2','installing'],
                ['text','pip install my app'],]



# SECTION: main app
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # main app config
        self.title(config.WINDOW_TITLE)
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.configure(bg=config.COLOR_BACKGOUND)
        
        # create a menu bar
        menubar = tk.Menu(self)
        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.cmd_barMenu_new)
        file_menu.add_command(label="Open", command=self.cmd_barMenu_open)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        # Add the file and edit menus to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)
        # Configure the app to use the menu bar
        self.config(menu=menubar)
        
        # create main frame
        self.main_frame = MainFrame(self)
        
    def cmd_barMenu_new(self):
        print('cmd_barMenu_new')

    def cmd_barMenu_open(self):
        print('cmd_barMenu_open')

             
        
# SECTION: main frame
class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=config.COLOR_BACKGOUND,
                        highlightbackground='#ff0000', highlightthickness=config.SHOW_FRAME_STROKE)

        # frame config
        self.pack(fill=tk.BOTH, expand=True)
        self.pack_propagate(False)

        # create list frame
        self.list_frame = ListFrame(self)
        self.list_frame.pack(padx=(10,0),pady=10,fill=tk.Y, side=tk.LEFT)
        
        # create element frame
        self.element_frame = ElementFrame(self)
        self.element_frame.pack(padx=10,pady=10,fill=tk.BOTH, side=tk.RIGHT, expand=True)       

        

# SECTION: list frame
class ListFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=config.ELEMENT_LIST_WIDTH, bg=config.COLOR_1,
                            highlightbackground='#3cc900', highlightthickness=config.SHOW_FRAME_STROKE)
        
        # frame config
        self.pack_propagate(False)
        
        # add headline
        self.label = tk.Label(self, text="Left Frame", bg=config.COLOR_1)
        self.label.pack(pady=10)
    
        
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Arial", 20))
        tree = ttk.Treeview(self, style="Custom.Treeview")
        tree.pack()

        # Add columns
        tree["columns"] = ("Index", "Type", "Content")

        # Define column properties
        tree.column("#0", width=40, minwidth=40)
        tree.column("#1", width=50, minwidth=30)
        tree.column("#2", width=50, minwidth=30)
        # # Create headings
        tree.heading("#0", text="Index", anchor="w")
        tree.heading("#1", text="Type", anchor="center")
        tree.heading("#2", text="Content", anchor="w")
        
        # Add sample elements
        for i in range(5):
            tree.insert("", "end", text=f"Item {i}", values=(i, "Type", f"Content {i}"))


        
    def on_button_click(self):
        # Handle button click in left frame
        pass



# SECTION: element frame
class ElementFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=config.COLOR_BACKGOUND,
                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE)
        
        # frame config
        self.pack_propagate(False)
        
        self.label = tk.Label(self, text="Right Frame")
        self.button = tk.Button(self, text="Right Button", command=self.on_button_click)
        
        self.label.pack(pady=10)
        self.button.pack(pady=10)
        
    def on_button_click(self):
        # Handle button click in right frame
        pass




# SECTION: run app
app = MainApp()
app.mainloop()
